from os import makedirs, getenv, getcwd, environ
from os.path import join
from glob import glob
from pathlib import Path

import pytest
import pymongo
from dotenv import load_dotenv
from bson.json_util import loads, dumps

from database.__init__ import db
from app import app


load_dotenv(verbose=True)


def load_test_db(backup_db_dir):
    makedirs(backup_db_dir, exist_ok=True)
    
    client = pymongo.MongoClient(
        host=getenv('MONGO_HOST'),
        port=int(getenv('MONGO_PORT')), 
        username=getenv('MONGO_USERNAME'),
        password=getenv('MONGO_PASSWORD')
    )
    database = client[getenv('MONGO_TEST_DBNAME')]
    collections = database.list_collection_names()

    for i, collection_name in enumerate(collections):
        col = getattr(database,collections[i])
        collection = col.find()
        jsonpath = collection_name + '.json'
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'wb') as jsonfile:
            jsonfile.write(dumps(collection).encode())

    client.close()


def restore_all_documents(backup_db_dir):
    collection_json_file_ls = glob(join(backup_db_dir, '*'))
    for collection_json_file_path in collection_json_file_ls:
        with open(collection_json_file_path, 'r') as file:
            data = file.read().replace('\n', '')
        data = loads(data)
        collection_name = Path(collection_json_file_path).stem
        if len(data) == 0:
            pass
        elif len(data) == 1:
            db.get_db()[collection_name].insert_one(data[0])
        else:
            db.get_db()[collection_name].insert_many(data)


def drop_all_documents():
    for collection_name in db.get_db().list_collection_names():
        db.get_db().drop_collection(collection_name)


test_backup_local_path = join(getcwd(), 'test_back_up')
load_test_db(test_backup_local_path)


@pytest.fixture(scope='function')
def client():
    drop_all_documents()
    restore_all_documents(test_backup_local_path)
    with app.test_client() as client:
        return client

