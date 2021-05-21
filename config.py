import os
from dotenv import load_dotenv


# set mongo uri
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, verbose=True)
else:
    raise Exception('.env does not exist.')

mongo_uri = os.getenv('MONGO_URI')


class Config:
    # Change the secret key in production run.
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False
    MONGO_URI = mongo_uri
    
    # For encoding korean language
    JSON_AS_ASCII = False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    DEBUG = False


config_by_name = {
    'dev' : DevConfig,
    'test' : TestConfig,
    'prod' : ProdConfig,
    'default' : DevConfig
}