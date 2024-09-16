# examples-playwright-started

This project is an example of Headless browser testing using Playwright.


## Table of Contents <!-- omit in toc -->

- [examples-playwright-started](#examples-playwright-started)
  - [See also](#see-also)
  - [Setup](#setup)
  - [Examples](#examples)
    - [Playwright for Python](#playwright-for-python)
  - [Development](#development)
    - [How the project was initialized](#how-the-project-was-initialized)


## See also

- <https://playwright.dev/python/>
- <https://github.com/microsoft/playwright-python>


## Setup

Install the required browsers:

```shell
playwright install
sudo ../../.venv/bin/playwright install-deps
```

## Examples

### Playwright for Python

- [Getting Started - Playwright for Python](https://playwright.dev/python/docs/intro)

See [these tests](./tests/) for more examples.


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
