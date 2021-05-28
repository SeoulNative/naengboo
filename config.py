import os


class Config:
    # Change the secret key in production run.
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False
    MONGO_URI = os.getenv('MONGO_URI')
    
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