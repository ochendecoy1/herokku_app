from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FileUploadPage(BasePage):
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")

    def upload_file(self, file_path: str):
        self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)

    def click_upload(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_uploaded_file_name(self):
        return self.driver.find_element(*self.UPLOADED_FILES).text
