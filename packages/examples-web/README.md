# examples-web

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
- [Get started](#get-started)
- [CommandLine HTTP servers](#commandline-http-servers)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)

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

- HTTPS servers:
  - `https_index_server.py` - Tiny HTTPS index server using `http.server`
  - `https_custom_handler_server.py` - Tiny HTTPS custom handler server using `http.server`

## CommandLine HTTP servers

For development purposes, you can start a simple server with `http.server`.

```shell
python -m http.server 9000
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
