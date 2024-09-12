"""Ignore HTTPS errors.

References:
    - https://playwright.dev/python/docs/test-runners#ignore-https-errors

Run tests:

    Start a dummy server on another terminal.
    Please prepare a certificate separately.

    ```shell
    python tools/https_server.py
    ```

    Test requires -m option:

    ```shell
    pytest tests/getting_started/test_xx_ignore_https_errors.py -m "use_other_env"
    ```
"""

from typing import Any

import pytest
from playwright.sync_api import Page, expect

"""If you set it to false, you will get an error.

    ```console
    playwright._impl._errors.Error: Page.goto: net::ERR_CERT_AUTHORITY_INVALID at https://127.0.0.1:8443/
    ```
"""
use_self_signed_certificate = True


# in conftest.py
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, Any]) -> dict[str, Any]:
    return (
        {**browser_context_args, "ignore_https_errors": True} if use_self_signed_certificate else browser_context_args
    )


@pytest.mark.use_other_env
def test_self_signed_site(page: Page) -> None:
    # use self-signed certificate site
    goto_site = "https://127.0.0.1:8443/"
    page.goto(goto_site)
    expect(page).to_have_url(goto_site)
