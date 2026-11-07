import time

import pytest
import time
from selenium.webdriver.common.keys import Keys

from conftest import BASE_URL
from pages.inputs_page import InputsPage


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.parametrize("value", ["1", "42", "-5", "3.14"])
def test_numeric_values_input(browser, value):
    page = InputsPage(browser, BASE_URL)
    page.open(page.PATH)

    page.type_text(value)
    # иначе не видно, что значение ввелось
    time.sleep(0.3)
    assert page.value() == value


@pytest.mark.advanced
@pytest.mark.regression
@pytest.mark.xfail(reason="input[type=number] не принимает буквы — это ожидаемое поведение")
def test_letters_are_rejected(browser):
    page = InputsPage(browser, BASE_URL)
    page.open(page.PATH)

    page.type_text("abc")
    assert page.value() == "abc"


@pytest.mark.advanced
@pytest.mark.regression
def test_arrow_up_increments_value(browser):
    page = InputsPage(browser, BASE_URL)
    page.open(page.PATH)

    page.type_text("10")
    page.press_arrow(Keys.ARROW_UP)
    assert page.value() == "11"


@pytest.mark.advanced
@pytest.mark.regression
def test_arrow_down_decrements_value(browser):
    page = InputsPage(browser, BASE_URL)
    page.open(page.PATH)

    page.type_text("10")
    page.press_arrow(Keys.ARROW_DOWN)
    assert page.value() == "9"
