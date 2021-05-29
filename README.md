# 냉장고를 부탁해(가제) - Backend

## Pre-requisites

- Python 3
- Poetry
<!-- - Mongodb -->

## Getting Started

### Installation

[check poetry official installation docs](https://python-poetry.org/docs/#installation)

```bash
# install poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# check installation
poetry --version

# install dependencies
poetry install
```

### Run

First, you must prepare the `.env` file in root directory.  
Please specify your app's environment variables in a .env file.

```python
# .env file example
FLASK_APP='app'

# configs: dev, test, prod, default(uses DevConfig)
FLASK_CONFIG='dev'

# mongodb conn format: 'mongodb://[username:password@]host[:port][/[defaultauthdb][?options]]'
# use single quote if you use ! in your string
MONGO_URI='mongodb://localhost:27017/naengboo'
```

```python
# execute virtualenv
poetry shell

# run flask server
flask run
```
