# examples-flask

An examples of Python web application using Flask.

## Table of Contents <!-- omit in toc -->

- [examples-flask](#examples-flask)
  - [References](#references)
  - [Examples](#examples)
  - [Getting started](#getting-started)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## References

- [Flask’s documentation](https://flask.palletsprojects.com/)

## Examples

- [Quickstart](./scripts/quickstart/README.md)
- [Tutorial - flaskr](./src/flaskr/README.md)
  
- [Modular Applications with Blueprints](./scripts/blueprints/README.md)

## Getting started

Install dependencies:

```shell
uv sync
```

Run service:

```shell
flask --app examples_flask run 
```

or using uwsgi:

```shell
uvx uwsgi --ini uwsgi.ini --venv $VIRTUAL_ENV
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-flask
uv add --project packages/examples-flask --dev pytest pytest-cov
uv add --project packages/examples-flask flask
uv add --project packages/examples-flask uwsgi

uv sync --all-packages
```
