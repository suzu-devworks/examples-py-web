# examples-flask-media

This project is an example of web media and streaming using Flask.

## Table of Contents <!-- omit in toc -->

- [Examples](#examples)
  - [Live streaming webcam](#live-streaming-webcam)
  - [Video streaming](#video-streaming)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
  - [ImportError: libGL.so.1](#importerror-libglso1)

## Examples

### Live streaming webcam

- [Webcam streaming example for MJPEG](./src/examples/webcam/mjpeg/README.md)
- [Webcam streaming example using HLS](./src/examples/webcam/hls/README.md)

### Video streaming

- [Chunked streaming of video files](./src/examples/video/chunks/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
rye init -p
rye add --dev pytest-cov
rye add flask flask-cors
rye add opencv-python
rye add --dev types-flask-cors

rye sync
```

### ImportError: libGL.so.1

```console
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

For debian based systems:

```shell
apt install -y libgl1-mesa-dev
```
