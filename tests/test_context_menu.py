import pytest

from pages.context_menu_page import ContextMenuPage


@pytest.fixture()
def context_menu_page(browser):
    return ContextMenuPage(browser, "http://the-internet.herokuapp.com")


def test_context_menu(context_menu_page):
    context_menu_page.open("/context_menu")

    context_menu_page.right_click_on_hotspot()

    assert context_menu_page.get_alert_text() == "You selected a context menu", (
        "текст не совпадает"
    )

    context_menu_page.accept_alert()
