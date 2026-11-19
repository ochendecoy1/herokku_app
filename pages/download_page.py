from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DownloadPage(BasePage):
    LINK = (By.CSS_SELECTOR, "a[href*='download']")

    def click_first_link(self):
        link = self.driver.find_element(*self.LINK)
        link.click()
        # имя файла берём из ссылки, чтобы не зависеть от текста на странице
        file_name = link.get_attribute("href").split("/")[-1]
        return file_name
