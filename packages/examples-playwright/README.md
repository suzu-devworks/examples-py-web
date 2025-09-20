# examples-playwright

This project is an example of end-to-end testing using Playwright.

## Table of Contents <!-- omit in toc -->

- [Install browsers](#install-browsers)
- [Examples](#examples)
- [Development](#development)
  - [How the project was initialized](#how-the-project-was-initialized)
- [References](#references)

## Install browsers

Install the required browsers and system dependencies:

```shell
playwright install --with-deps chromium
```

## Examples

- [Getting Started](./tests/playwright_getting_started/README.md)
- [API reference](./tests/playwright_references/README.md)

## Development

### How the project was initialized

This project was initialized with the following command:

```shell
uv init --lib packages/examples-playwright
uv add --project packages/examples-playwright --dev pytest pytest-cov pytest-asyncio pytest-xdist
uv add --project packages/examples-playwright --dev pytest-playwright
uv add --project packages/examples-playwright --dev pytest-httpserver trustme

uv sync --all-packages
```

## References

- <https://playwright.dev/python>
- <https://github.com/microsoft/playwright-python>
