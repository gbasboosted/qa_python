"""Проверки переходов по логотипам в шапке сайта."""

import allure

from pages.main_page import MainPage
from urls import BASE_URL, ORDER_URL


@allure.feature("Навигация по логотипам")
class TestLogoNavigation:
    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_opens_main_page(self, driver):
        page = MainPage(driver)
        page.open(ORDER_URL)

        page.click_scooter_logo()

        assert page.get_current_url().rstrip("/") == BASE_URL
        assert page.is_main_page_open()

    @allure.title("Логотип Яндекса открывает Дзэн в новом окне")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        page = MainPage(driver).open_main_page()

        page.click_yandex_logo()

        assert page.is_dzen_open()
