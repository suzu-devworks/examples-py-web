# examples-flask-media

## Table of Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Setup](#setup)
  - [Run](#run)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
  - [ImportError](#importerror)

## Overview

This project is an example of web media and streaming using Flask.

### Setup

Select the python interpreter to use:

```shell
pdm use
```

Get the dependent packages:

```shell
pdm sync
```

### Run

Run the server:

```shell
flask --app examples_flask_media run
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
pdm new --no-git packages/examples-flask-media --python .venv/bin/python -n
pdm add --dev -e packages/examples-flask-media/
pdm add --project packages/examples-flask-media/ flask opencv-python

# pdm.lock updates
pdm install
```

### ImportError

Here's what to do if you get these errors:

```console
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory
```

For debian based systems:

```shell
apt install -y libgl1-mesa-dev libgthread
```
<!-- // spell-checker:words libgl1 libgthread -->
