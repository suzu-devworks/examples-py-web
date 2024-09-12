# examples-flask-started

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

Flask web programming examples. The very basics.


## Table of Contents <!-- omit in toc -->

- [examples-flask-started](#examples-flask-started)
  - [See also](#see-also)
  - [Setup](#setup)
  - [Flask web apps](#flask-web-apps)
    - [Quickstart](#quickstart)
    - [Tutorial (flaskr)](#tutorial-flaskr)
    - [Blueprint example](#blueprint-example)
  - [How the project was initialized](#how-the-project-was-initialized)


## See also

- [Flask’s documentation](https://flask.palletsprojects.com/)


## Setup

Install the dependencies.

```shell
pdm install
```

## Flask web apps

### Quickstart

- [Quickstart - Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

Run the quickstart, for example:

```shell
 flask --app src.quickstart._01_hello run --debug
```

See [the code header](./src/quickstart/) for more examples.


### Tutorial (flaskr)

- [Tutorial - Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/)

Create database:

```shell
flask --app flaskr init-db
```

Run service:

```shell
flask --app flaskr run --debug
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

See [the code header](./src/flaskr/) for more examples.


### Blueprint example

Let's see how it changes depending on the Blueprint's `static_folder` and `template_folder`.

- [Blueprint - Flask](https://flask.palletsprojects.com/en/3.0.x/blueprints/)

Run service:

```shell
flask --app blueprints run --debug
```

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

See [the code header](./src/blueprints/) for more examples.


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init --dist -n
pdm add -d flake8 mypy black isort pyclean
pdm add -d pytest-cov
pdm add flask
```
