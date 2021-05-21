from flask import Flask
from app.extensions import api
from config import config_by_name
import pymongo, mongomock


db = None


def register_extensions(app):
    api.init_app(app)


def init_db(app):
    global db

    MONGO_URI = app.config['MONGO_URI']
    if MONGO_URI is None:
        raise Exception('MONGO_URI not exist in .env file')
    parsed_uri = pymongo.uri_parser.parse_uri(MONGO_URI)
    db_name = parsed_uri["database"]

    if app.config['TESTING']:
        client = mongomock.MongoClient(MONGO_URI)
    else:
        client = pymongo.MongoClient(MONGO_URI)
    db = client[db_name]


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    init_db(app)
    register_extensions(app)

    from app.views.recipes import Recipes
    from app.views.refrigerators import Refrigerators
    from app.views.user import User

    api.add_namespace(Recipes, '/recipes')
    api.add_namespace(Refrigerators, '/refrigerators')
    api.add_namespace(User, '/user')

    return app

