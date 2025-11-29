# examples-flask-blueprint

## Table of Contents <!-- omit in toc -->

- [Blueprint example](#blueprint-example)
  - [Install the dependencies](#install-the-dependencies)
  - [Start the app in development mode](#start-the-app-in-development-mode)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Blueprint example

Let's see how it changes depending on the Blueprint's `static_folder` and `template_folder`.

- [Blueprint - Flask](https://flask.palletsprojects.com/en/3.0.x/blueprints/)

### Install the dependencies

Run on the root (examples-py-web directory):

```shell
pdm venv create  
pdm use
pdm install 
```

### Start the app in development mode

```shell
flask --app examples_flask_blueprint run --debug
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

# examples-flask-blueprint
mkdir -p packages/examples-flask-blueprint
cd packages/examples-flask-blueprint
pdm init --no-git --dist -n
pdm add flask

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-blueprint
```
