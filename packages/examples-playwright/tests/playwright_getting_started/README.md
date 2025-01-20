# Getting Started

## Table of Contents <!-- omit in toc -->

- [Getting Started](#getting-started)
  - [References](#references)
  - [Installation](#installation)
  - [Writing tests](#writing-tests)
  - [Generating tests](#generating-tests)
    - [Running Codegen](#running-codegen)
    - [Recording a test](#recording-a-test)
    - [Generating locators](#generating-locators)
  - [Running and debugging tests](#running-and-debugging-tests)
    - [Debugging tests](#debugging-tests)
  - [Trace viewer](#trace-viewer)
  - [Setting up CI](#setting-up-ci)
  - [Pytest Plugin Reference](#pytest-plugin-reference)
    - [Examples](#examples)

## References

- <https://playwright.dev/python/docs/intro>

## Installation

Install the Pytest plugin:

```shell
pip install pytest-playwright
```

Install the required browsers:

```shell
playwright install
```

Browser and OS dependencies are installed with one command:

```shell
playwright install --with-deps chromium
```

See all supported browsers:

```shell
playwright install --help
```

## Writing tests

- [First test](./test_example.py)
- Actions
- Assertions
  - [Test isolation](./writing/test_example_isolation.py)
  - [Using fixtures](./writing/test_example_using_fixtures.py)

## Generating tests

### Running Codegen

<!-- spell-checker: words todomvc -->
```shell
playwright codegen demo.playwright.dev/todomvc
```

For Mac, you need [XQuartz](https://www.xquartz.org/)

### Recording a test

1. Change the target in the Playwright inspector to `Pytest`
2. Actions like click or fill by simply interacting with the page
3. Assertions by clicking on one of the icons in the toolbar and then clicking on an element on the page to assert against
4. When you have finished interacting with the page, press the 'record' button to stop
5. Use the 'copy' button to copy the generated code to your editor
6. Use the clear button to clear the code to start recording again
7. Once finished, close the Playwright inspector window or stop the terminal command

### Generating locators

1. Press the 'Record' button to stop the recording
2. Click on the 'Pick Locator' button and then hover over elements in the browser window to see the locator highlighted underneath each element
3. Click on an element will display the element's locator in the Locator window
4. Use the copy button to copy the locator and paste it into your code

## Running and debugging tests

### Debugging tests

```shell
PWDEBUG=1 pytest -s test_example.py
```

## Trace viewer

Recording a trace:

```shell
pytest --tracing on
```

This will record the trace and place it into the file named `trace.zip` in your test-results directory.

Opening the trace:

```shell
playwright show-trace trace.zip
```

## Setting up CI

See [playwright.yml](../../../../.github/workflows/playwright.yml)

## Pytest Plugin Reference

### Examples

- [Using multiple contexts](./examples/_01_override_browser_context_args/)
- [Using multiple contexts](./examples/_02_using_multiple_contexts/)
- [Skip test by browser](./examples/_03_skip_by_browser/)
- [Run on a specific browser](./examples/_04_specific_browser/)
- [Ignore HTTPS errors](./examples/_05_ignore_https_errors/)
- [Use custom viewport size](./examples//_06_custom_viewport_size/)
- [Device emulation / BrowserContext option overrides](./examples/_07_device_emulation/)
