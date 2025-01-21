"""Playwright(Async).

References:
    - https://playwright.dev/python/docs/api/class-playwright

Run tests:

    ```shell
    pytest tests/playwright_references/test_playwright_async.py
    ```

Run:

    ```shell
    python tests/playwright_references/test_playwright_async.py
    ```
"""

import asyncio

import pytest
from playwright.async_api import Playwright, async_playwright


@pytest.mark.skip(reason="because async causes launch() to freeze.")
@pytest.mark.asyncio
async def test_run(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await test_run(playwright)


if __name__ == "__main__":
    asyncio.run(main())
