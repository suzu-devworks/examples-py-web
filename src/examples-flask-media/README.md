# examples-flask-media

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

This project is an example of web media and streaming using Flask.


## Getting started

Move to this folder and install the dependencies.

```shell
cd examples-flask-media
pdm install
```

## Index

### Live streaming webcam 

- [Webcam streaming example for MJPEG](./src/examples/webcam/mjpeg/README.md)

### Video streaming

- [Chunked streaming of video files](./src/examples/video/chunks/README.md)


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init
pdm add -d flake8 mypy black isort pytest-cov pyclean
pdm add flask
pdm add flask-cors
pdm add opencv-python

pdm add -d types-flask-cors
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
