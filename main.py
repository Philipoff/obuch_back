from flask import Flask, request, jsonify
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
    print(user_type, theme, article, material_type)
    return "Hello"


app.run(debug=True)
