from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FramesPage(BasePage):
    IFRAME_ID = "mce_0_ifr"
    TEXT_AREA = (By.ID, "tinymce")

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.IFRAME_ID)

    def get_frame_text(self):
        return self.driver.find_element(*self.TEXT_AREA).text.strip()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
