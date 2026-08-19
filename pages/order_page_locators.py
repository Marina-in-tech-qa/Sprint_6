from selenium.webdriver.common.by import By

class OrderPageLocators:

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