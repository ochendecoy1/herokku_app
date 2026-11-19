from selenium.webdriver.common.by import By

from pages.base_page import BasePage

PARAGRAPHS = (By.TAG_NAME, "p")

VARIANT_OK = "Sometimes you'll see a typo, other times you won't."
VARIANT_TYPO = "Sometimes you'll see a typo, other times you won,t."
KNOWN_VARIANTS = (VARIANT_OK, VARIANT_TYPO)


class TyposPage(BasePage):
    PATH = "/typos"

    def paragraphs(self) -> list:
        return self.driver.find_elements(*PARAGRAPHS)

    def paragraph_text(self) -> str:
        # работаю только со вторым абзацем, ибо опечатка может быть только в нём
        return self.paragraphs()[1].text
