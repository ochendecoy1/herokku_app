from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")
    ENABLE_BUTTON = (By.XPATH, "//button[contains(text(),'Enable')]")
    MESSAGE = (By.ID, "message")
    CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")

    def click_remove(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()

    def click_enable(self):
        self.driver.find_element(*self.ENABLE_BUTTON).click()

    def wait_for_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MESSAGE)
        )
        return element.text

    def is_checkbox_present(self):
        # find_elements не бросает исключение — возвращает список
        return len(self.driver.find_elements(*self.CHECKBOX)) > 0

    def is_input_enabled(self):
        return self.driver.find_element(*self.INPUT_FIELD).is_enabled()
