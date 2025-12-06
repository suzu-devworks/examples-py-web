# examples-flask

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
- [Examples](#examples)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

## Overview

This project is an examples of Python web application using Flask.

- [Flask’s documentation](https://flask.palletsprojects.com/)

## Get started

Select the python interpreter to use:

```shell
pdm use
```

Get the dependent packages:

```shell
pdm sync
```

## Examples

- [Quickstart](./examples/quickstart/README.md)

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
