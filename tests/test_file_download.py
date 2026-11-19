import pytest

from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait

from pages.download_page import DownloadPage


@pytest.fixture()
def download_page(browser):
    return DownloadPage(browser, "http://the-internet.herokuapp.com")


def test_file_download(download_page, download_dir):
    download_page.open("/download")

    # Кликаем по первой ссылке, получаем имя файла
    file_name = download_page.click_first_link()
    downloaded_file = download_dir / file_name

    # Ждём завершения скачивания: файл существует и нет временного .crdownload
    def download_finished(driver):
        return downloaded_file.exists() and not Path(str(downloaded_file) + ".crdownload").exists()

    WebDriverWait(download_page.driver, 30).until(download_finished)

    assert downloaded_file.exists(), f"Файл не скачался: {downloaded_file}"
    assert downloaded_file.stat().st_size > 0, "Файл скачался, но пустой"
