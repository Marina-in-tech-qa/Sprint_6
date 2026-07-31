from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    TOP_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"
    )

    COOKIE_BUTTON = (
        By.ID,
        "rcc-confirm-button"
    )

    FAQ_SECTION = (
        By.XPATH,
        "//div[text()='Вопросы о важном']"
    )

    SCOOTER_LOGO = (
        By.XPATH,
        "//img[@alt='Scooter']"
    )

    YANDEX_LOGO = (
        By.XPATH,
        "//img[@alt='Yandex']"
    )

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
        self.click(self.COOKIE_BUTTON)
        

    def click_top_order_button(self):
        self.click(self.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.scroll_to_element(self.BOTTOM_ORDER_BUTTON)
        self.click(self.BOTTOM_ORDER_BUTTON)

    def scroll_to_faq(self):
        self.scroll_to_element(self.FAQ_SECTION)

    def click_question(self, index):
        locator = self.question_locator(index)
        self.scroll_to_element(locator)
        self.click_with_js(locator)

    def get_answer_text(self, index):
        return self.get_text(
            self.answer_locator(index)
        )

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)