from os import path
from json import loads
from pathlib import Path

from glob import glob
import pytest

from test.mock import mock_data_dict
import app


flask_context = app.create_app()


if 'mongomock' not in str(app.db['_store']):
    raise Exception('Pytest requires test(mock) db')
    

@pytest.fixture(scope='function')
def client():
    with flask_context.test_client() as client:
        insert_mock_data()
        yield client
        flush_db()


def flush_db():
    for collection_name in app.db.list_collection_names():
        app.db.drop_collection(collection_name)


def insert_mock_data():
    for mock_item in mock_data_dict.items():
        collection_name = mock_item[0]
        data = mock_item[1]

        if len(data) == 0:
            pass
        elif len(data) == 1:
            app.db[collection_name].insert_one(data[0])
        else:
            app.db[collection_name].insert_many(data)