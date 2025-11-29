# examples-flask-tutorial

## Table of Contents <!-- omit in toc -->

- [Tutorial - Flaskr](#tutorial---flaskr)
  - [Install the dependencies](#install-the-dependencies)
  - [Create database](#create-database)
  - [Start the app in development mode](#start-the-app-in-development-mode)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Tutorial - Flaskr

- [Tutorial - Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/)

### Install the dependencies

Run on the root (examples-py-web directory):

```shell
pdm venv create  
pdm use
pdm install 
```

### Create database

```shell
flask --app flaskr init-db
```

### Start the app in development mode

```shell
flask --app flaskr run --debug
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
#examples-py-web
pdm init --no-git -n
pdm add -d flake8 mypy black isort pytest-cov pyclean

# examples-flask-quickstart
mkdir -p packages/examples-flask-tutorial
cd packages/examples-flask-tutorial
pdm init --no-git --dist -n
pdm add flask

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-tutorial
```
