from os import path
from glob import glob
from json import loads
from pathlib import Path


def load_documents():
    mock_data_dict = {}
    
    collection_json_file_path = path.join(path.dirname(__file__), "data", '*')
    collection_json_file_ls = glob(collection_json_file_path)

    for collection_json_file_path in collection_json_file_ls:
        with open(collection_json_file_path, 'r') as file:
            data = file.read()
            data = loads(data)
    
        collection_name = Path(collection_json_file_path).stem
        mock_data_dict[collection_name] = data
    
    return mock_data_dict

mock_data_dict = load_documents()