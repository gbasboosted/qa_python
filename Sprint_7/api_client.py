"""Небольшой клиент для вызова ручек Яндекс Самоката."""

import allure
import requests

from urls import Urls


REQUEST_TIMEOUT = 30


class CourierApi:
    @staticmethod
    @allure.step("Создать курьера")
    def create(payload):
        return requests.post(Urls.COURIER, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Авторизовать курьера")
    def login(payload):
        return requests.post(
            Urls.COURIER_LOGIN,
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )

    @staticmethod
    @allure.step("Удалить курьера с id={courier_id}")
    def delete(courier_id):
        return requests.delete(
            f"{Urls.COURIER}/{courier_id}",
            timeout=REQUEST_TIMEOUT,
        )


class OrderApi:
    @staticmethod
    @allure.step("Создать заказ")
    def create(payload):
        return requests.post(Urls.ORDERS, json=payload, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Получить список заказов")
    def get_list(params=None):
        return requests.get(Urls.ORDERS, params=params, timeout=REQUEST_TIMEOUT)

    @staticmethod
    @allure.step("Получить заказ по track={track}")
    def get_by_track(track=None):
        params = None if track is None else {"t": track}
        return requests.get(
            Urls.ORDER_BY_TRACK,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

    @staticmethod
    @allure.step("Принять заказ id={order_id} курьером id={courier_id}")
    def accept(order_id="", courier_id=None):
        params = None if courier_id is None else {"courierId": courier_id}
        return requests.put(
            f"{Urls.ACCEPT_ORDER}/{order_id}",
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

    @staticmethod
    @allure.step("Отменить заказ с track={track}")
    def cancel(track):
        return requests.put(
            Urls.CANCEL_ORDER,
            params={"track": track},
            timeout=REQUEST_TIMEOUT,
        )
