# examples-flask-started

Flask web programming examples. The very basics.


## Table of Contents <!-- omit in toc -->

- [examples-flask-started](#examples-flask-started)
  - [Examples](#examples)
    - [Quickstart](#quickstart)
    - [Tutorial (flaskr)](#tutorial-flaskr)
    - [Blueprint example](#blueprint-example)
  - [Learn more](#learn-more)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)


## Examples

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


## Learn more

- [Flask’s documentation](https://flask.palletsprojects.com/)


## Development

### How the project was initialized

This project was initialized with the following command:

```shell
rye init
rye add --dev pytest-cov
rye add flask

rye sync
```
