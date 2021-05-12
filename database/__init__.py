
import os
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv

load_dotenv(verbose=True)
app = Flask(__name__)
if os.getenv("TEST") is None:
    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('MONGO_DBNAME'),
        'host': os.getenv('MONGO_HOST'),
        'port': int(os.getenv('MONGO_PORT')),
        'username': os.getenv('MONGO_USERNAME'),
        'password': os.getenv('MONGO_PASSWORD'),
    }
else:
    app.config["MONGODB_HOST"] = "mongomock://localhost/test"
db = MongoEngine(app)