import os
from dotenv import load_dotenv

def load_file(path: str) -> None:
    dotenv_path = os.path.join(os.getcwd(), path) # ~/naengboo/path

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise Exception('File path: ' + path + ' does not exist.')
