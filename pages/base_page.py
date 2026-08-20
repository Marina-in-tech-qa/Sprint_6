import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти кликабельный элемент")
    def find_clickable_element(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Нажать на элемент")
    def click(self, locator):
        self.find_clickable_element(locator).click()

    @allure.step("Нажать на элемент через JavaScript")
    def click_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def write(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)

        self.driver.execute_script(
            """
            arguments[0].scrollIntoView({
                block: 'center'
            });
            """,
            element
        )

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_element_to_disappear(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться перехода на указанный URL")
    def wait_for_url(self, url):
        self.wait.until(
            EC.url_to_be(url)
        )

    @allure.step("Дождаться появления части URL")
    def wait_for_url_contains(self, part):
        self.wait.until(
            EC.url_contains(part)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить список открытых окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на другое окно")
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step("Дождаться открытия нового окна")
    def wait_for_new_window(self, old_windows):
        self.wait.until(
            lambda driver:
            len(driver.window_handles) > len(old_windows)
        )