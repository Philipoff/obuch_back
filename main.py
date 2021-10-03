import json
import wikipedia
import urllib.request

from bson import json_util
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

from key_words import find_keys
from get_info import get_info
from request_word import get_url

app = Flask(__name__)
cors = CORS(app)
wikipedia.set_lang("ru")

client = MongoClient(
    "mongodb+srv://MindlessDoc:NfhrjdNjg228@cluster0.jlpdf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")

db_name = "Obuch"
collection_compilations = client[db_name]["compilations"]
collection_rating = client[db_name]["rating"]
collection_themes = client[db_name]["themes"]
collection_blocked_sites = client[db_name]["blocked_sites"]


# collection_compilations.insert_one({
#     "name": "имя учителя",
#     "grade": "Учитель начальных",
#     "desc": "Описание",
#     "links": [
#         {"link": "Ссылка",
#          "name": "имя",
#          "description": "Пипиьсика",
#          "pic": "url картинки"}]
# })


@app.route("/getsearchresults", methods=["GET", "POST"])
def getsearchresults():
    form = request.get_json()
    user_type = form["user_type"]
    theme = form["theme"]
    article = form["article"]
    material_type = form["material_type"]
    try:
        wikipedia.page(theme.title())
        return {
            "title": wikipedia.search(theme)[0],
            "type": "wiki",
            "text": wikipedia.summary(theme.title())
        }
    except wikipedia.exceptions.PageError as e:
        print("Не нашлось, да и ничего страшного")

    theme_item = collection_themes.find_one({"theme": theme})
    if theme_item:
        collection_themes.update_one({"theme": theme}, {"$inc": {"count": +1}})
    else:
        collection_themes.insert_one({
            "theme": theme,
            "count": 1
        })

    urls = get_url(theme)
    urls_to_find = find_keys(article)
    for url in urls_to_find:
        urls += get_url(url)

    urls = list(set(urls))

    rating = []
    is_blocked = []
    for url in urls:
        url = url.split("/")[2].replace("www.", '')
        site = collection_rating.find_one({"site": url})
        if site:
            rating.append(int(site["rating"]))
        else:
            collection_rating.insert_one({
                "site": url,
                "rating": 0
            })
            rating.append(0)
        if collection_blocked_sites.find_one({"site": url}):
            is_blocked.append(1)
        else:
            is_blocked.append(0)
    urls = list(map(get_info, urls))
    for i in range(len(urls)):
        urls[i]["rating"] = rating[i]
        urls[i]["is_blocked"] = is_blocked[i]
    if user_type == 1:
        return jsonify({
            "urls": urls
        })
    else:
        urls = [url for url in urls if url["rating"] >= -5 and url["is_blocked"] == 0]
        urls = sorted(urls, reverse=True, key=lambda x: x["rating"])
        return jsonify({
            "urls": urls
        })


@app.post("/rate_site")
def rate_site():
    form = request.get_json()
    url = form["url"]
    vote = form["vote"]
    site = url.split("/")[2].replace("www.", "")
    if vote == 0:
        vote -= 1
    existing = collection_rating.find_one({"site": site})["rating"]
    collection_rating.update_one({"site": site}, {"$set": {
        "rating": existing + vote
    }})
    return "Success"


@app.post("/block_site")
def block_site():
    form = request.get_json()
    site = form["url"].split("/")[2].replace("www.", '')
    reason = form["reason"]
    collection_blocked_sites.insert_one({
        "site": site,
        "reason": reason
    })
    return "Success"


@app.get("/get_compilation/<id>")
def get_compilation(id):
    collection = collection_compilations.find_one({"_id": ObjectId(id)})
    return json.loads(json_util.dumps(collection))


app.run(debug=True)
