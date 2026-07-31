import allure
from pages.main_page import MainPage
from urls import BASE_URL, ORDER_URL, DZEN_URL_PART

@allure.feature("Logo")
@allure.title("Переход на главную страницу по логотипу Самокат")
def test_scooter_logo_redirects_to_main_page(driver):
    main_page = MainPage(driver)

    main_page.open(ORDER_URL)
    main_page.click_scooter_logo()
    main_page.wait_for_url(BASE_URL)

    assert main_page.get_current_url() == BASE_URL

@allure.feature("Logo")
@allure.title("Переход на Дзен по логотипу Яндекс")
def test_yandex_logo_opens_dzen_in_new_window(driver):
    main_page = MainPage(driver)

    main_page.open(BASE_URL)

    old_windows = main_page.get_window_handles()

    main_page.click_yandex_logo()

    main_page.wait.until(
        lambda current_driver:
        len(current_driver.window_handles) > len(old_windows)
    )

    new_windows = main_page.get_window_handles()
    new_window = next(
        window for window in new_windows
        if window not in old_windows
    )

    main_page.switch_to_window(new_window)
    main_page.wait_for_url_contains(DZEN_URL_PART)

    assert DZEN_URL_PART in main_page.get_current_url()
