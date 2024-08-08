"""Playwright(Sync).

References:
    - https://playwright.dev/python/docs/api/class-playwright

Run tests:

    ```shell
    pytest tests/references/test_playwright_sync.py
    ```

Run:

    ```shell
    python tests/references/test_playwright_sync.py
    ```
"""

from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        test_run(playwright)
