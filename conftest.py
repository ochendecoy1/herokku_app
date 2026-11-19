import tempfile
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://the-internet.herokuapp.com"


@pytest.fixture()
def browser(download_dir):
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": str(download_dir),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    })

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

# фикстура для временной папки скачанных файлов
@pytest.fixture()
def download_dir():
    path = Path(tempfile.mkdtemp())
    yield path
