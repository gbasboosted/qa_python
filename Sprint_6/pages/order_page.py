"""Page Object двухшаговой формы заказа самоката."""

from datetime import date, timedelta

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Адрес: куда привезти заказ']",
    )
    METRO_INPUT = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    PHONE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Далее']")
    DELIVERY_DATE_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='* Когда привезти самокат']",
    )
    DURATION_DROPDOWN = (By.CSS_SELECTOR, ".Dropdown-control")
    COMMENT_INPUT = (
        By.CSS_SELECTOR,
        "input[placeholder='Комментарий для курьера']",
    )
    SUBMIT_ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[last()]",
    )
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_MODAL_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') "
        "and contains(normalize-space(), 'Заказ оформлен')]",
    )

    @allure.step("Получить локатор станции метро {station}")
    def metro_option(self, station):
        return (
            By.XPATH,
            "//button[.//div[normalize-space()=" + repr(station) + "]]",
        )

    @allure.step("Получить локатор срока аренды {duration}")
    def duration_option(self, duration):
        return (
            By.XPATH,
            "//div[contains(@class, 'Dropdown-option') "
            "and normalize-space()=" + repr(duration) + "]",
        )

    @allure.step("Заполнить данные получателя")
    def fill_customer_form(self, order):
        self.type_text(self.FIRST_NAME_INPUT, order["first_name"])
        self.type_text(self.LAST_NAME_INPUT, order["last_name"])
        self.type_text(self.ADDRESS_INPUT, order["address"])
        self.type_text(self.PHONE_INPUT, order["phone"])
        self.type_text(self.METRO_INPUT, order["station"])
        self.click(self.metro_option(order["station"]))
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполнить параметры аренды")
    def fill_rental_form(self, order):
        delivery_date = date.today() + timedelta(
            days=order["delivery_in_days"]
        )
        date_input = self.find_visible(self.DELIVERY_DATE_INPUT)
        date_input.send_keys(delivery_date.strftime("%d.%m.%Y"))
        date_input.send_keys(Keys.ESCAPE)

        self.click(self.DURATION_DROPDOWN)
        self.click(self.duration_option(order["duration"]))
        self.click((By.ID, order["color"]))
        self.type_text(self.COMMENT_INPUT, order["comment"])

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click(self.SUBMIT_ORDER_BUTTON)
        self.click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def success_message(self):
        return self.text_of(self.SUCCESS_MODAL_TITLE)
