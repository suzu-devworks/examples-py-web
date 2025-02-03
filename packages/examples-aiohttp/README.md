# examples-aiohttp

An example Python Web application using AIOHTTP.

## Table of Contents <!-- omit in toc -->

- [examples-aiohttp](#examples-aiohttp)
  - [References](#references)
  - [Examples](#examples)
  - [Run development server](#run-development-server)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## References

- [Welcome to AIOHTTP](https://docs.aiohttp.org/en/stable/index.html#)
- [Third Party Libraries](https://docs.aiohttp.org/en/stable/third_party.html)

## Examples

- Server
  - [Quickstart](./scripts/servers/quickstart/README.md)

## Run development server

Using CLI:

```shell
python -m aiohttp.web -H localhost -P 8000 scripts.servers.quickstart._01_simple:create_app
```

Using aiohttp-devtools

```shell
adev runserver --host localhost -p 8000 --app-factory create_app scripts/servers/quickstart/_01_simple.py
```

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-aiohttp
uv add --project packages/examples-aiohttp "aiohttp[speedups]" aiohttp-session aiohttp-jinja2
uv add --project packages/examples-fastapi --dev aiohttp-devtools
```
