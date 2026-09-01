"""Позитивные сценарии оформления заказа."""

import allure
import pytest

from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Успешный заказ через кнопку {entry_point}")
    @pytest.mark.parametrize(
        "order_data, entry_point",
        [
            (ORDER_DATA[0], "top"),
            (ORDER_DATA[1], "bottom"),
        ],
        ids=["top-button-first-customer", "bottom-button-second-customer"],
    )
    def test_order_can_be_created(
        self,
        driver,
        order_data,
        entry_point,
    ):
        main_page = MainPage(driver).open_main_page()
        main_page.start_order(entry_point)

        order_page = OrderPage(driver)
        order_page.fill_customer_form(order_data)
        order_page.fill_rental_form(order_data)
        order_page.submit_order()

        assert "Заказ оформлен" in order_page.success_message()
