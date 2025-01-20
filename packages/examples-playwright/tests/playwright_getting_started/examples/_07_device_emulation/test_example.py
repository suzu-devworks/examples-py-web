from playwright.sync_api import Page


def test_emulation_info(page: Page) -> None:
    # spell-checker:words KHTML
    assert (
        page.evaluate("window.navigator.userAgent")
        == "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.2 Mobile/15E148 Safari/604.1"
    )
    assert page.evaluate("window.screen.width") == 393
    assert page.evaluate("window.screen.height") == 659
