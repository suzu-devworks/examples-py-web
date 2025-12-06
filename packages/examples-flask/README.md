# examples-flask

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
  - [Setup](#setup)
  - [Run flaskr](#run-flaskr)
- [Examples](#examples)
  - [User’s Guide](#users-guide)
  - [Others](#others)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Overview

This project is an examples of Python web application using Flask.

- [Flask’s documentation](https://flask.palletsprojects.com/)

## Get started

### Setup

Select the python interpreter to use:

```shell
pdm use
```

Get the dependent packages:

```shell
pdm sync
```

### Run flaskr

Create a database:

```shell
flask --app flaskr init-db
```

Run the server:

```shell
flask --app flaskr run 
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Examples

### User’s Guide

- [Quickstart](./examples/quickstart/README.md)
- [Tutorial - flaskr](./src/flaskr/README.md)
- [Modular Applications with Blueprints](./examples/blueprints/README.md)

### Others

- [Encodings](./examples/encodings/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
pdm new --no-git packages/examples-flask --python .venv/bin/python -n
pdm add --dev -e packages/examples-flask/
pdm add --project packages/examples-flask/ flask
pdm add --project packages/examples-flask/ pytest --dev pytest-cov

# pdm.lock updates
pdm install
```
