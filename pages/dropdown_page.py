from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage

DROPDOWN = (By.ID, "dropdown")


class DropdownPage(BasePage):
    PATH = "/dropdown"

    @property
    def select(self) -> Select:
        return Select(self.driver.find_element(*DROPDOWN))

    def all_options(self) -> list:
        return [option.text for option in self.select.options]

    def select_by_text(self, text: str):
        self.select.select_by_visible_text(text)

    def selected_text(self) -> str:
        return self.select.first_selected_option.text
