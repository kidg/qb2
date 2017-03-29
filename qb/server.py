# -*- coding:utf8 -*-
# AUTHOR = 'kiddguo'
from flask import Flask
from settings import MONGO_URI, MONGO_DATABASE
from flask import render_template
import pymongo

app = Flask(__name__)

@app.route('/')
def hello():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[MONGO_DATABASE]
    jokes = db["QbItem"].find()
    client.close()
    return render_template("qb.html", jokes=jokes)

if __name__ == '__main__':
    app.run()