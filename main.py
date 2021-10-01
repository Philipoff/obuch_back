from flask import Flask, request
from pymongo import MongoClient
from request_word import get_url
from key_words import find_keys

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://MindlessDoc:NfhrjdNjg228@cluster0.jlpdf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db_name = "Obuch"
collection_name = "rating"
collection = client[db_name][collection_name]


@app.post("/send_values")
def send_values():
    form = request.get_json()
    user_type = form["user_type"]
    theme = form["theme"]
    article = form["article"]
    material_type = form["material_type"]

    urls = get_url(theme)
    urls_to_find = find_keys(article)
    for url in urls_to_find:
        urls += get_url(url)

    for url in urls:
        url = url.split("/")[2].replace("www.", "")
        print(url)
    return "Hello"


app.run(debug=True)
