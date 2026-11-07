from selenium.webdriver.common.by import By

from pages.base_page import BasePage

ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
DELETE_BUTTONS = (By.XPATH, "//button[text()='Delete']")


class AddRemoveElementsPage(BasePage):
    PATH = "/add_remove_elements/"

    def add_element(self):
        self.driver.find_element(*ADD_BUTTON).click()

    def delete_element(self):
        self.driver.find_element(*DELETE_BUTTONS).click()

    def delete_buttons_count(self) -> int:
        return len(self.driver.find_elements(*DELETE_BUTTONS))
