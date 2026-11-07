import pytest

from pages.checkboxes_page import CheckboxesPage
from conftest import BASE_URL


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
def test_first_checkbox_unchecked_then_checked(browser):
    page = CheckboxesPage(browser, BASE_URL)
    page.open(page.PATH)

    first = page.checkboxes()[0]
    assert page.is_checked(first) is False

    first.click()
    assert page.is_checked(first) is True


@pytest.mark.basic
@pytest.mark.regression
def test_second_checkbox_checked_then_unchecked(browser):
    page = CheckboxesPage(browser, BASE_URL)
    page.open(page.PATH)

    second = page.checkboxes()[1]
    assert page.is_checked(second) is True

    second.click()
    assert page.is_checked(second) is False
