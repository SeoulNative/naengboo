# 냉장고를 부탁해(가제) - Backend

## Pre-requisites

- Python 3
- Poetry
<!-- - Mongodb -->

## Getting Started

### Installation

Before installation, you must prepare the `.env` file in root directory.

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

```python
# check env
vim .env

# execute virtualenv
poetry shell

# run flask server
flask run
```

## Q&A

### Vscode unresolved import lint

맨 처음 vscode의 작업 폴더를 naengboo로 열었을 때,  
특정 absolute path import 문에서 unresolved import lint가 발생합니다(Pylance).  
그 이유는 Pylance가 import path search하는 root 폴더가 기본적으로 open한 폴더이기 때문입니다.

2가지 해결 방법이 있습니다.

1. `~/naengboo/app` 폴더로 열어서 작업한다
2. pylance setting을 수정한다.

2번째 방법에 대한 자세한 설명입니다.

1. vscode에서 ctrl+shift+P
2. language specific settings 선택
3. python 선택
4. setting.json 파일 에디터에서 열어지면
5. **`"python.analysis.extraPaths":["[여러분의 naengboo 폴더 경로]/naengboo/app"],`** 추가
   1. ex) `Users/myuser/naengboo/app`

```json
...
"python.languageServer": "Pylance",
"python.analysis.extraPaths":["[여러분의 naengboo 폴더 경로]/naengboo/app"],
"terminal.integrated.fontFamily": "'D2Coding'",
"git.enableSmartCommit": true,
...
```
