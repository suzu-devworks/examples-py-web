# examples-playwright-started

This project is an example of Headless browser testing using Playwright.


## Table of Contents <!-- omit in toc -->

- [examples-playwright-started](#examples-playwright-started)
  - [Setup](#setup)
  - [Examples](#examples)
    - [Getting Started](#getting-started)
  - [Learn more](#learn-more)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)


## Setup

Install the required browsers:

```shell
playwright install
sudo ../../.venv/bin/playwright install-deps
```

## Examples

### Getting Started

- [Getting Started - Playwright for Python](https://playwright.dev/python/docs/intro)

See [these tests](./tests/).


## Learn more

- <https://playwright.dev/python/>
- <https://github.com/microsoft/playwright-python>


## Development

### How the project was initialized

This project was initialized with the following command:

```shell
rye init
rye add --dev pytest-cov pytest-asyncio

rye add playwright
rye add --dev pytest-playwright

rye sync
```
