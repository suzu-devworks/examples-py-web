# examples-flask-tutorial

## Table of Contents <!-- omit in toc -->

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
#examples-py-web
pdm init --no-git -n
pdm add -d flake8 mypy black isort pytest-cov pyclean

# examples-flask-quickstart
mkdir -p packages/examples-flask-tutorial
cd packages/examples-flask-tutorial
pdm init --no-git --dist -n
pdm add flask

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-quickstart
```
