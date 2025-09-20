# examples-aiohttp

An example Python Web application using AIOHTTP.

## Table of Contents <!-- omit in toc -->

- [Examples](#examples)
- [Run development server](#run-development-server)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
  - [Third Party Libraries](#third-party-libraries)
- [References](#references)

## Examples

- Server
  - [Quickstart](./scripts/servers/quickstart/README.md)
  - [Nested applications](./scripts/servers/nested_apps/README.md)

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

### Third Party Libraries

The libraries I use in this project are:

- [aiohttp-devtools](https://github.com/aio-libs/aiohttp-devtools)
- [aiohttp-session](https://github.com/aio-libs/aiohttp-session)
- [aiohttp-jinja2](https://github.com/aio-libs/aiohttp-jinja2)

## References

- [Welcome to AIOHTTP](https://docs.aiohttp.org/en/stable/index.html#)
- [Third-Party libraries](https://docs.aiohttp.org/en/stable/third_party.html)
