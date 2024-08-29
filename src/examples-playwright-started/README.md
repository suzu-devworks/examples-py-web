# examples-playwright-started

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

This project is an example of Headless browser testing using Playwright.


## Table of Contents <!-- omit in toc -->

- [examples-playwright-started](#examples-playwright-started)
  - [See also](#see-also)
  - [Setup](#setup)
  - [Playwright for Python](#playwright-for-python)
  - [How the project was initialized](#how-the-project-was-initialized)


## See also

- <https://playwright.dev/python/>
- <https://github.com/microsoft/playwright-python>


## Setup

Install the dependencies:

```shell
pdm install
```

Install the required browsers:

```shell
playwright install
sudo ../../.venv/bin/playwright install-deps
```

## Playwright for Python

- [Getting Started - Playwright for Python](https://playwright.dev/python/docs/intro)

See [these tests](./tests/) for more examples.


## How the project was initialized

This project was initialized with the following command:

```shell
pdm init -n
pdm add -d flake8 mypy black isort pyclean
pdm add -d pytest-cov pytest-asyncio

pdm add playwright
pdm add -d pytest-playwright
```
