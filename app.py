from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "thisisasecret"
app.config["MONGO_URI"] = "mongodb://localhost:27017/apidemo2019"
mongo = PyMongo(app)