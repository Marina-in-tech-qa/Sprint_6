import allure

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

    @allure.step("Открыть главную страницу")
    def open_main_page(self, url):
        self.open(url)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать верхнюю кнопку «Заказать»")
    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step("Нажать нижнюю кнопку «Заказать»")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Прокрутить страницу к разделу FAQ")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Открыть вопрос FAQ №{index}")
    def click_question(self, index):
        locator = self.question_locator(index)
        self.scroll_to_element(locator)
        self.click_with_js(locator)

    @allure.step("Получить ответ на вопрос FAQ №{index}")
    def get_answer_text(self, index):
        return self.get_text(
            self.answer_locator(index)
        )

    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)