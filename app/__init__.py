from flask import Flask
from pymongo import MongoClient, uri_parser
from app.extensions import api
from config import config_by_name


db = None


def register_extensions(app):
    # Registers flask extensions
    api.init_app(app)


def init_db(app):
    global db

    MONGO_URI = app.config['MONGO_URI']
    parsed_uri = uri_parser.parse_uri(MONGO_URI)
    db_name = parsed_uri["database"]
    print("MONGO_URI:", MONGO_URI)

    client = MongoClient(MONGO_URI)
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

