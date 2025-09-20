# examples-flask

An examples of Python web application using Flask.

## Table of Contents <!-- omit in toc -->

- [Examples](#examples)
- [Getting started](#getting-started)
- [Deploy](#deploy)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
- [References](#references)

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

It will be hosted at the following URL:

- <http://127.0.0.1:5000/>

## Deploy

Use `uwsgi`

```shell
uvx uwsgi --ini uwsgi.ini --venv $VIRTUAL_ENV
```

> [!WARNING]
> The uwsgi package will be rebuilt during installation,
> so you will need to install gcc and python3-dev.

For NGINX:

```js
    location ~ ^/dev/(.*)$ {
      include uwsgi_params;
      uwsgi_param SCRIPT_NAME /dev;
      uwsgi_param PATH_INFO /$1;
      set $uwsgi_pass_server dev:3031;
      uwsgi_pass $uwsgi_pass_server;
    }
```

Setting `PATH_INFO` will rewrite the path to forward.

Also, set `$uwsgi_pass_server` to check at the time of request so that nginx will start even if the upstream is not running.

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-flask
uv add --project packages/examples-flask --dev pytest pytest-cov
uv add --project packages/examples-flask flask

uv sync --all-packages
```

## References

- [Flask’s documentation](https://flask.palletsprojects.com/)
