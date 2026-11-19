from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    HOTSPOT = (By.ID, "hot-spot")

    def right_click_on_hotspot(self):
        ActionChains(self.driver).context_click(
            self.driver.find_element(*self.HOTSPOT)
        ).perform()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
