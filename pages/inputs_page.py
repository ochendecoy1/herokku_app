from selenium.webdriver.common.by import By

from pages.base_page import BasePage

INPUT = (By.TAG_NAME, "input")


class InputsPage(BasePage):
    PATH = "/inputs"

    def input_field(self):
        return self.driver.find_element(*INPUT)

    def type_text(self, text: str):
        field = self.input_field()
        field.clear()
        field.send_keys(text)

    def value(self) -> str:
        return self.input_field().get_attribute("value")

    def press_arrow(self, key):
        self.input_field().send_keys(key)
