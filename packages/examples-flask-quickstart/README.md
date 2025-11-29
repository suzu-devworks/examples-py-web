# examples-flask-quickstart

## Table of Contents <!-- omit in toc -->

- [Quickstart](#quickstart)
  - [Install the dependencies](#install-the-dependencies)
  - [Start the app in development mode](#start-the-app-in-development-mode)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Quickstart

- [Quickstart - Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

### Install the dependencies

Run on the root (examples-py-web directory):

```shell
pdm venv create  
pdm use
pdm install 
```

### Start the app in development mode

```shell
flask --app examples_flask_quickstart._01_hello run --debug
```

See [the code header](./src/examples_flask_quickstart/) for more examples:

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
#examples-py-web
pdm init --no-git -n
pdm add -d flake8 mypy black isort pytest-cov pyclean

# examples-flask-quickstart
mkdir -p packages/examples-flask-quickstart
cd packages/examples-flask-quickstart
pdm init --no-git --dist -n
pdm add flask

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-quickstart
```
