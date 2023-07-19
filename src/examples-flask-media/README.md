# examples-flask-media

Flask Web video audio media programming examples.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

## Setup

Clone the repository:

```shell
clone https://github.com/suzu-devworks/examples-py-web.git

cd examples-py-web

```

Create a virtualenv in advance:

```shell
python -m venv .venv
. .venv/bin/activate

python -m pip install --upgrade pip
pip install pdm

```

Here's how this project is setup:

```shell
cd src/examples-flask-media

# select interpreter
pdm use

# install dependencies and self.
pdm install

```

## Create project

This project was generated with the command:

```shell
mkdir -p src/examples-flask-media
cd src/examples-flask-media

# create new pyproject.toml
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean

pdm add flask
pdm add flask-cors
pdm add opencv-python

pdm add -d types-flask-cors
```

## troubleshooting

### ImportError: libGL.so.1: cannot open shared object file: No such file or directory

```shell
apt install -y libgl1-mesa-dev
```
