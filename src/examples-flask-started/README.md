# examples-flask-started

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

Flask web programming examples. The very basics.


## These became textbooks 

- https://flask.palletsprojects.com/


## Getting started

Move to this folder and install the dependencies.

```shell
cd examples-flask-started
pdm use
pdm install
```

### Quickstart 
<!-- // spell-checker:words Quickstart -->

- [Quickstart - Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

Run the quickstart, for example:

```shell
 flask --app src.quickstart._01_hello run --debug
```

See [the code header](./src/quickstart/) for more examples:


### flaskr - Tutorial

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

- http://127.0.0.1:5000/


### Blueprint example

Let's see how it changes depending on the Blueprint's `static_folder` and `template_folder`.

- [Blueprint - Flask](https://flask.palletsprojects.com/en/3.0.x/blueprints/)

Run service:

```shell
flask --app blueprints run --debug
```

It will be hosted at the following URL:

- http://127.0.0.1:5000/


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean
pdm add flask
```
