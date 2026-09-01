"""Базовые действия, общие для страниц сервиса."""

from urllib.parse import urlparse

import allure
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости элемента")
    def find_visible(self, locator):
        return self.wait.until(conditions.visibility_of_element_located(locator))

    @allure.step("Дождаться доступности элемента для клика")
    def find_clickable(self, locator):
        return self.wait.until(conditions.element_to_be_clickable(locator))

    @allure.step("Нажать на элемент")
    def click(self, locator):
        element = self.find_clickable(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element = self.wait.until(conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def text_of(self, locator):
        return self.find_visible(locator).text

    @allure.step("Нажать на элемент, если он отображается")
    def click_if_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                conditions.element_to_be_clickable(locator)
            ).click()
            return True
        except TimeoutException:
            return False

    @allure.step("Получить список открытых окон")
    def get_window_handles(self):
        return set(self.driver.window_handles)

    @allure.step("Переключиться в новое окно")
    def switch_to_new_window(self, old_handles):
        self.wait.until(
            lambda driver: len(driver.window_handles) > len(old_handles)
        )
        new_handle = next(
            handle
            for handle in self.driver.window_handles
            if handle not in old_handles
        )
        self.driver.switch_to.window(new_handle)

    @allure.step("Дождаться URL, содержащего {fragment}")
    def wait_for_url_contains(self, fragment):
        return self.wait.until(conditions.url_contains(fragment))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Дождаться открытия домена {domain}")
    def wait_for_domain(self, domain, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: (
                urlparse(driver.current_url).hostname or ""
            ).endswith(domain)
        )
