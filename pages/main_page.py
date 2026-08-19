from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @staticmethod
    def question_locator(index):
        return (
            By.ID,
            f"accordion__heading-{index}"
        )

    @staticmethod
    def answer_locator(index):
        return (
            By.ID,
            f"accordion__panel-{index}"
        )

    def open_main_page(self, url):
        self.open(url)

    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)
        

    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    def click_question(self, index):
        locator = self.question_locator(index)
        self.scroll_to_element(locator)
        self.click_with_js(locator)

    def get_answer_text(self, index):
        return self.get_text(
            self.answer_locator(index)
        )

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)