import pytest

from pages.add_remove_elements_page import AddRemoveElementsPage
from conftest import BASE_URL


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_add_two_elements_and_delete_one(browser):
    page = AddRemoveElementsPage(browser, BASE_URL)
    page.open(page.PATH)

    page.add_element()
    page.add_element()
    assert page.delete_buttons_count() == 2

    page.delete_element()
    assert page.delete_buttons_count() == 1


@pytest.mark.advanced
@pytest.mark.regression
def test_delete_all_added_elements(browser):
    page = AddRemoveElementsPage(browser, BASE_URL)
    page.open(page.PATH)

    for _ in range(3):
        page.add_element()
    for _ in range(3):
        page.delete_element()

    assert page.delete_buttons_count() == 0
