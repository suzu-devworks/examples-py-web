# examples-flask-media

## Table of Contents <!-- omit in toc -->

- [Examples](#examples)
  - [Install the dependencies](#install-the-dependencies)
  - [Start the app in development mode](#start-the-app-in-development-mode)
  - [Live streaming webcam](#live-streaming-webcam)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
- [Troubleshooting](#troubleshooting)
  - [ImportError: libGL.so.1](#importerror-libglso1)

## Examples

### Install the dependencies

Run on the root (examples-py-web directory):

```shell
pdm venv create  
pdm use
pdm install 
```

### Start the app in development mode

Run on project directory:

```shell
pdm run dev
```

### Live streaming webcam

- [Webcam streaming example for MJPEG](./src/examples_flask_media/webcam/mjpeg/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
#examples-py-web
pdm init --no-git -n
pdm add -d flake8 mypy black isort pytest-cov pyclean

# examples-flask-media
mkdir -p packages/examples-flask-media
cd packages/examples-flask-media
pdm init --no-git --dist -n
pdm add flask
pdm add opencv-python

rm pdm.lock
cd ../../

pdm add -d -e packages/examples-flask-media
```

## Troubleshooting

### ImportError: libGL.so.1

```console
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

For debian based systems:

```shell
apt install -y libgl1-mesa-dev
```
<!-- // spell-checker:words libgl1 -->
