import pytest
import allure

from data import FIRST_ORDER, SECOND_ORDER
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL


@allure.feature("Order")
class TestOrder:

    @allure.title("Оформление заказа с набором данных: {order_data[name]}")
    @pytest.mark.parametrize(
        "order_data",
        [FIRST_ORDER, SECOND_ORDER]
    )
    def test_create_order(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_name(order_data["name"])
        order_page.fill_surname(order_data["surname"])
        order_page.fill_address(order_data["address"])
        order_page.select_metro_station(order_data["metro"])
        order_page.fill_phone(order_data["phone"])
        order_page.click_next()

        order_page.fill_delivery_date(order_data["date"])
        order_page.select_rental_period(order_data["rent"])

        if order_data["color"] == "black":
            order_page.choose_black_scooter()
        else:
            order_page.choose_grey_scooter()

        order_page.fill_comment(order_data["comment"])
        order_page.click_order()
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_success_text()