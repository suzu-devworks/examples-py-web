# examples-playwright-started

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

This project is an example of Headless browser testing using Playwright.


## More document

- https://playwright.dev/python/
- https://github.com/microsoft/playwright-python


## Getting started

Move to this folder and install the dependencies.

```shell
cd examples-playwright-started
pdm install
playwright install
sudo ../../.venv/bin/playwright install-deps
```

## Playwright for Python

- [Getting Started - Playwright for Python](https://playwright.dev/python/docs/intro)

Run tests:

```shell
pdm run test
```

See [these tests](./tests/) for more examples:


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init
pdm add -d flake8 mypy black isort pytest-cov pytest-asyncio pyclean

pdm add playwright
pdm add -d pytest-playwright
```
