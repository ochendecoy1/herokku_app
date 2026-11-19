from selenium.webdriver.common.by import By

from pages.base_page import BasePage

CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")


class CheckboxesPage(BasePage):
    PATH = "/checkboxes"

    def checkboxes(self) -> list:
        return self.driver.find_elements(*CHECKBOXES)

    @staticmethod
    def is_checked(checkbox) -> bool:
        return checkbox.is_selected()
