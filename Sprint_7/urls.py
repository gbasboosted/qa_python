"""Адреса API учебного сервиса Яндекс Самокат."""


class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    COURIER = f"{BASE_URL}/courier"
    COURIER_LOGIN = f"{COURIER}/login"

    ORDERS = f"{BASE_URL}/orders"
    ACCEPT_ORDER = f"{ORDERS}/accept"
    CANCEL_ORDER = f"{ORDERS}/cancel"
    ORDER_BY_TRACK = f"{ORDERS}/track"
