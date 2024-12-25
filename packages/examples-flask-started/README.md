# examples-flask-started

Flask web programming examples. Learn based on the Flask document.

## Table of Contents <!-- omit in toc -->

- [examples-flask-started](#examples-flask-started)
  - [Examples](#examples)
  - [Learn more](#learn-more)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## Examples

- [Quickstart](./src/quickstart/README.md)
- [Tutorial - flaskr](./src/flaskr/README.md)
- [Modular Applications with Blueprints](./src/blueprints/README.md)

## Learn more

- [Flask’s documentation](https://flask.palletsprojects.com/)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --package packages/examples-flask-started
uv add --project packages/examples-flask-started --dev pytest pytest-cov
uv add --project packages/examples-flask-started flask

uv sync --all-packages
```
