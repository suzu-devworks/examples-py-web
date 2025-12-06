# examples-web

## Table of Contents <!-- omit in toc -->

## Overview

This project is an example of web programming using Python.

## Get started

Select the python interpreter to use:

```shell
pdm use
```

Get the dependent packages:

```shell
pdm sync
```

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
# examples-py-web
pdm use
pdm init --no-git -n
pdm add -d flake8 mypy black isort pyclean

# examples-web
pdm new --no-git packages/examples-web --python .venv/bin/python -n
pdm add -d -e packages/examples-web/

# pdm.lock updates
pdm install
```
