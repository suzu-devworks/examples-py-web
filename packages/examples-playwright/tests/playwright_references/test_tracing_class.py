"""Tracing.

References:
    - https://playwright.dev/docs/api/class-tracing

Run tests:

    ```shell
    pytest tests/playwright_references/test_tracing_class.py
    ```

    Opening the trace:

    ```shell
    playwright show-trace trace.zip
    ```
"""

from playwright.sync_api import Playwright


def test_start(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto("https://playwright.dev")
    context.tracing.stop(path="trace.zip")


def test_start_chunk(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()
    page.goto("https://playwright.dev")

    context.tracing.start_chunk()
    page.get_by_text("Get Started").click()
    # Everything between start_chunk and stop_chunk will be recorded in the trace.
    context.tracing.stop_chunk(path="trace1.zip")

    context.tracing.start_chunk()
    page.goto("http://example.com")
    # Save a second trace file with different actions.
    context.tracing.stop_chunk(path="trace2.zip")
