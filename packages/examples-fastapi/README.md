# examples-fastapi

An example Python Web API application using FastAPI.

## Table of Contents <!-- omit in toc -->

- [Examples](#examples)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
- [References](#references)

## Examples

- [Example](./scripts/home/README.md)
- [FastAPI Tutorial](./scripts/tutorials/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-fastapi
uv add --project packages/examples-fastapi "fastapi[standard]"
uv add --project packages/examples-fastapi PyJWT "passlib[bcrypt]"
uv add --project packages/examples-fastapi --dev types-passlib
```

## References

- [FastAPI framework](https://fastapi.tiangolo.com/)
