from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):

    NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Станция метро']"
    )

    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Далее']"
    )

    DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )

    RENTAL_PERIOD = (
        By.XPATH,
        "//div[text()='* Срок аренды']"
    )

    COMMENT_INPUT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"
    )

    YES_BUTTON = (
        By.XPATH,
        "//button[text()='Да']"
    )

    BLACK_SCOOTER = (
        By.XPATH,
        "//label[text()='чёрный жемчуг']"
    )

    GREY_SCOOTER = (
        By.XPATH,
        "//label[text()='серая безысходность']"
    )

    RENTAL_PERIOD = (
        By.XPATH,
        "//div[text()='* Срок аренды']"
    )

    ORDER_SUCCESS = (
        By.XPATH,
        "//div[contains(text(),'Заказ оформлен')]"
    )
    

    def fill_name(self, name):
        self.write(self.NAME_INPUT, name)

    def fill_surname(self, surname):
        self.write(self.SURNAME_INPUT, surname)

    def fill_address(self, address):
        self.write(self.ADDRESS_INPUT, address)

    def fill_phone(self, phone):
        self.write(self.PHONE_INPUT, phone)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    @staticmethod
    def metro_station_locator(station):
        return(By.XPATH, f"//*[text()='{station}']")

    def select_metro_station(self, station):
        self.write(self.METRO_INPUT, station)
        self.click(self.metro_station_locator(station))

    #Дата
    def fill_delivery_date(self, date):
        date_input = self.find_element(self.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    #Комментарий
    def fill_comment(self, comment):
        self.write(self.COMMENT_INPUT, comment)

    #Цвет
    def choose_black_scooter(self):
        self.click(self.BLACK_SCOOTER)

    def choose_grey_scooter(self):
        self.click(self.GREY_SCOOTER)

    #Заказать
    def click_order(self):
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.YES_BUTTON)

    #Выбор срока аренды
    @staticmethod
    def rental_period_locator(period):
        return (
            By.XPATH,
            f"//div[text()='{period}']"
        )

    def select_rental_period(self, period):
        self.click(self.RENTAL_PERIOD)
        self.click(self.rental_period_locator(period))

    
    def get_success_text(self):
        return self.get_text(self.ORDER_SUCCESS)