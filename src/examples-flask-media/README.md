# examples-flask-media

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

This project is an example of web media and streaming using Flask.

## Table of Contents <!-- omit in toc -->

- [examples-flask-media](#examples-flask-media)
  - [Setup](#setup)
  - [Flask media apps](#flask-media-apps)
    - [Live streaming webcam](#live-streaming-webcam)
    - [Video streaming](#video-streaming)
  - [How the project was initialized](#how-the-project-was-initialized)
  - [Troubleshooting](#troubleshooting)
    - [ImportError: libGL.so.1](#importerror-libglso1)

## Setup

Install the dependencies.

```shell
pdm install
```

## Flask media apps

### Live streaming webcam

- [Webcam streaming example for MJPEG](./src/examples/webcam/mjpeg/README.md)
- [Webcam streaming example using HLS](./src/examples/webcam/hls/README.md)

### Video streaming

- [Chunked streaming of video files](./src/examples/video/chunks/README.md)


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init --dist -n
pdm add -d flake8 mypy black isort pyclean
pdm add -d pytest-cov
pdm add flask
pdm add flask-cors
pdm add opencv-python
pdm add types-flask-cors
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
