import pytest

from conftest import BASE_URL
from pages.dropdown_page import DropdownPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.regression
class TestDropdown:

    def test_all_options_present(self, dropdown_page_class):
        options = dropdown_page_class.all_options()
        assert "Please select an option" in options
        assert "Option 1" in options
        assert "Option 2" in options

    def test_select_first_option(self, dropdown_page_class):
        dropdown_page_class.select_by_text("Option 1")
        assert dropdown_page_class.selected_text() == "Option 1"

    def test_select_second_option(self, dropdown_page_class):
        dropdown_page_class.select_by_text("Option 2")
        assert dropdown_page_class.selected_text() == "Option 2"


@pytest.mark.advanced
@pytest.mark.regression
def test_default_option_not_selectable(browser):
    page = DropdownPage(browser, BASE_URL)
    page.open(page.PATH)
    options = page.all_options()
    assert "Please select an option" in options
    page.select_by_text("Option 1")
    assert page.selected_text() == "Option 1"
