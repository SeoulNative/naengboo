from flask import Flask
from flask_mongoengine import MongoEngine
from .db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': "naengboo",
    'host': '3.36.96.53',
    'port': 27017,
    'username': 'theseoulnative',
    'password': ''
}
db = MongoEngine(app)
