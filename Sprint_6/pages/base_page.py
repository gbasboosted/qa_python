"""Базовые действия, общие для страниц сервиса."""

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

    def find_visible(self, locator):
        return self.wait.until(conditions.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(conditions.element_to_be_clickable(locator))

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

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator):
        return self.find_visible(locator).text

    def click_if_visible(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                conditions.element_to_be_clickable(locator)
            ).click()
            return True
        except TimeoutException:
            return False

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
