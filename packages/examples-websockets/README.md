# examples-websockets

This project is an example of Python WebSocket programming using websockets.

## Table of Contents <!-- omit in toc -->

- [examples-websockets](#examples-websockets)
  - [References](#references)
  - [Examples](#examples)
    - [Home](#home)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## References

- <https://websockets.readthedocs.io/>

## Examples

- [Home](#home)
- How-to guides
  - [Quickstart](./quickstart/README.md)

### Home

Here is an example echo server and a corresponding client, only demonstrating asyncio here.

start websocket server:

```shell
uv run asyncio/server.py 
```

start client:

```shell
uv run asyncio/client.py 
```

Also, websockets provides an interactive client:

```shell
uv run -m websockets ws://localhost:8765/
```

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --app packages/examples-websockets
uv add --project packages/examples-websockets websockets

uv sync --all-packages
```
