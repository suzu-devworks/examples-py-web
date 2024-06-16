"""Using fixtures.

References:
    - https://playwright.dev/python/docs/writing-tests#using-fixtures

Run tests:

    ```shell
    pytest tests/getting_started/test_02_isolation.py
    ```
"""

from playwright.sync_api import Page, expect


def test_example_test(page: Page) -> None:
    expect(page).to_have_url("about:blank")

    page.goto("https://playwright.dev/")
    expect(page).to_have_url("https://playwright.dev/")
    pass
    # "page" belongs to an isolated BrowserContext, created for this specific test.


def test_another_test(page: Page) -> None:
    expect(page).to_have_url("about:blank")
    pass
    # "page" in this second test is completely isolated from the first test.
