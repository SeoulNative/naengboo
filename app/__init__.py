from flask import Flask
from app.extensions import api
from config import config_by_name
import pymongo, mongomock, dotenv, os


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
        print('MongoDB initialized with mongomock')
    else:
        client = pymongo.MongoClient(MONGO_URI)
        print('MongoDB initialized with', parsed_uri['nodelist'][0][0]) # mongo host ip
    db = client[db_name]


def create_app():
    dotenv_path = os.path.join(os.getcwd(), ".env") # ~/naengboo/.env
    if os.path.exists(dotenv_path):
        dotenv.load_dotenv()
    else:
        raise Exception('.env file does not exist.')

    app = Flask(__name__)
    config_name = os.getenv("FLASK_CONFIG") or "default"
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

