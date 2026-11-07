import os

import pytest
from selenium import webdriver

BASE_URL = "http://the-internet.herokuapp.com"


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS"):
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
# фикстура на класс из доп задания
def dropdown_page_class():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    from pages.dropdown_page import DropdownPage
    page = DropdownPage(driver, BASE_URL)
    page.open(page.PATH)
    yield page
    driver.quit()
