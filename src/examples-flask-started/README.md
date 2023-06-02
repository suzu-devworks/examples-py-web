# examples-flask-started

Flask web programming examples.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## References

- https://flask.palletsprojects.com/

## Setup

Clone the repository:

```shell
clone https://github.com/suzu-devworks/examples-py-web.git

cd examples-py-web

```

Create a virtualenv in advance:

```shell
python -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip
pip install pdm

```

Here's how this project is setup:

```shell
cd src/examples-flask-started

# select interpreter
pdm use

# install dependencies and self.
pdm install

```

Create database:

```shell
flask --app flaskr init-db
```

## Create project

This project was generated with the command:

```shell
mkdir -p src/examples-flask-started
cd src/examples-flask-started

# create new pyproject.toml
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean

pdm add flask

```
