from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
 
    def fill_name(self, name):
        self.write(OrderPageLocators.NAME_INPUT, name)

    def fill_surname(self, surname):
        self.write(OrderPageLocators.SURNAME_INPUT, surname)

    def fill_address(self, address):
        self.write(OrderPageLocators.ADDRESS_INPUT, address)

    def fill_phone(self, phone):
        self.write(OrderPageLocators.PHONE_INPUT, phone)

    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @staticmethod
    def metro_station_locator(station):
        return(By.XPATH, f"//*[text()='{station}']")

    def select_metro_station(self, station):
        self.write(OrderPageLocators.METRO_INPUT, station)
        self.click(self.metro_station_locator(station))

    #Дата
    def fill_delivery_date(self, date):
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    #Комментарий
    def fill_comment(self, comment):
        self.write(OrderPageLocators.COMMENT_INPUT, comment)

    #Цвет
    def choose_black_scooter(self):
        self.click(OrderPageLocators.BLACK_SCOOTER)

    def choose_grey_scooter(self):
        self.click(OrderPageLocators.GREY_SCOOTER)

    #Заказать
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.YES_BUTTON)

    #Выбор срока аренды
    @staticmethod
    def rental_period_locator(period):
        return (
            By.XPATH,
            f"//div[text()='{period}']"
        )

    def select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD)
        self.click(self.rental_period_locator(period))

    
    def get_success_text(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS)