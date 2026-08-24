from selenium.webdriver.common.by import By

class MainPageLocators:
        
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