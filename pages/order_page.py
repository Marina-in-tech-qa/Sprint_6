import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить имя: {name}")
    def fill_name(self, name):
        self.write(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Заполнить фамилию: {surname}")
    def fill_surname(self, surname):
        self.write(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step("Заполнить адрес: {address}")
    def fill_address(self, address):
        self.write(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Заполнить номер телефона")
    def fill_phone(self, phone):
        self.write(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Нажать кнопку «Далее»")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @staticmethod
    def metro_station_locator(station):
        return (
            By.XPATH,
            f"//*[text()='{station}']"
        )

    @allure.step("Выбрать станцию метро: {station}")
    def select_metro_station(self, station):
        self.write(OrderPageLocators.METRO_INPUT, station)
        self.click(self.metro_station_locator(station))

    @allure.step("Выбрать дату доставки: {date}")
    def fill_delivery_date(self, date):
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Заполнить комментарий")
    def fill_comment(self, comment):
        self.write(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Выбрать чёрный цвет самоката")
    def choose_black_scooter(self):
        self.click(OrderPageLocators.BLACK_SCOOTER)

    @allure.step("Выбрать серый цвет самоката")
    def choose_grey_scooter(self):
        self.click(OrderPageLocators.GREY_SCOOTER)

    @allure.step("Нажать кнопку «Заказать»")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.YES_BUTTON)

    @staticmethod
    def rental_period_locator(period):
        return (
            By.XPATH,
            f"//div[text()='{period}']"
        )

    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(self.rental_period_locator(period))

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS)