import os
from dotenv import load_dotenv

def load_file(path: str) -> None:
    # naengboo/utils/../path = naengboo/path
    dotenv_path = os.path.join(os.path.dirname(__file__), "../" + path)

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise Exception('File path: ' + path + ' does not exist.')
