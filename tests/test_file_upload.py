import os
import tempfile
import time
import pytest

from pages.file_upload_page import FileUploadPage

FILE_NAME = "test_upload.txt"

# фикстура создания файла и удаления после теста
@pytest.fixture()
def test_file():
    dir_path = tempfile.mkdtemp()
    file_path = os.path.join(dir_path, FILE_NAME)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Содержимое тестового файла для загрузки")
    yield file_path
    os.remove(file_path)


@pytest.fixture()
def file_upload_page(browser):
    return FileUploadPage(browser, "http://the-internet.herokuapp.com")


def test_file_upload(file_upload_page, test_file):
    file_upload_page.open("/upload")

    file_upload_page.upload_file(test_file)
    file_upload_page.click_upload()
    time.sleep(3)
    assert file_upload_page.get_uploaded_file_name() == FILE_NAME, (
        f"Имя загруженного файла не совпало: '{file_upload_page.get_uploaded_file_name()}'"
    )
