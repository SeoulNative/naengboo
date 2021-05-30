from os import path
from json import loads
from pathlib import Path

from glob import glob
import pytest

import app


flask_context = app.create_app()
db = app.db


if "mongomock" not in str(app.db["_store"]):
    raise Exception("Pytest requires test(mock) db")
    

@pytest.fixture(scope='function')
def client():
    with flask_context.test_client() as client:
        load_documents()
        yield client
        flush_db()


def flush_db():
    for collection_name in db.list_collection_names():
        db.drop_collection(collection_name)


def load_documents():
    collection_json_file_path = path.join(path.dirname(__file__), "mock_data", '*')
    collection_json_file_ls = glob(collection_json_file_path)
    for collection_json_file_path in collection_json_file_ls:
        with open(collection_json_file_path, 'r') as file:
            data = file.read()
            data = loads(data)

        collection_name = Path(collection_json_file_path).stem

        if len(data) == 0:
            pass
        elif len(data) == 1:
            db[collection_name].insert_one(data[0])
        else:
            db[collection_name].insert_many(data)
    