# examples-flask

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
  - [Setup](#setup)
  - [Run flaskr](#run-flaskr)
- [Examples](#examples)
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

- [Quickstart](./examples/quickstart/README.md)
- [Encodings](./examples/encodings/README.md)
- [Tutorial - flaskr](./src/flaskr/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
pdm new --no-git packages/examples-flask --python .venv/bin/python -n
pdm add -d -e packages/examples-flask/
pdm add -p packages/examples-flask/ flask

# pdm.lock updates
pdm install
```
