# examples-fastapi

An example Python Web API application using FastAPI.

## Table of Contents <!-- omit in toc -->

- [examples-fastapi](#examples-fastapi)
  - [References](#references)
  - [Examples](#examples)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)

## References

- [FastAPI framework](https://fastapi.tiangolo.com/)

## Examples

- [Example](./scripts/home/README.md)
- [FastAPI Tutorial](./scripts/tutorials/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-fastapi
uv add --project packages/examples-fastapi "fastapi[standard]"
```
