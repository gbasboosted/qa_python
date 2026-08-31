"""Page Object главной страницы «Яндекс.Самоката»."""

from urllib.parse import urlparse

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from urls import BASE_URL, DZEN_DOMAIN


class MainPage(BasePage):
    TOP_ORDER_BUTTON = (By.XPATH, "(//button[normalize-space()='Заказать'])[1]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[normalize-space()='Заказать'])[2]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    SCOOTER_LOGO = (By.XPATH, "//a[.//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[.//img[@alt='Yandex']]")
    MAIN_PAGE_TITLE = (By.CSS_SELECTOR, "div[class*='Home_Header']")

    ORDER_BUTTONS = {
        "top": TOP_ORDER_BUTTON,
        "bottom": BOTTOM_ORDER_BUTTON,
    }

    def faq_question(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def faq_answer(self, index):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(BASE_URL)
        self.click_if_visible(self.COOKIE_BUTTON)
        return self

    @allure.step("Открыть ответ на вопрос №{index}")
    def open_faq_answer(self, index):
        self.click(self.faq_question(index))
        return self.text_of(self.faq_answer(index))

    @allure.step("Начать заказ через кнопку {position}")
    def start_order(self, position):
        self.click(self.ORDER_BUTTONS[position])
        self.wait.until(conditions.url_contains("/order"))

    @allure.step("Перейти по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    @allure.step("Открыть Дзэн по логотипу Яндекса")
    def click_yandex_logo(self):
        old_handles = set(self.driver.window_handles)
        self.click(self.YANDEX_LOGO)
        self.switch_to_new_window(old_handles)

    def is_main_page_open(self):
        return self.find_visible(self.MAIN_PAGE_TITLE).is_displayed()

    def is_dzen_open(self):
        return WebDriverWait(self.driver, 30).until(
            lambda driver: (
                urlparse(driver.current_url).hostname or ""
            ).endswith(DZEN_DOMAIN)
        )
