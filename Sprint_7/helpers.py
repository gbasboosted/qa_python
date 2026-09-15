"""Генераторы независимых тестовых данных."""

import random
import string
from datetime import date, timedelta


def generate_random_string(length=10):
    """Возвращает случайную строку из строчных латинских букв."""
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_courier_payload():
    suffix = generate_random_string()
    return {
        "login": f"courier_{suffix}",
        "password": f"password_{suffix}",
        "firstName": f"name_{suffix}",
    }


def generate_order_payload(color=None):
    suffix = generate_random_string(8)
    payload = {
        "firstName": "Иван",
        "lastName": "Тестов",
        "address": f"Москва, Тестовая улица, {random.randint(1, 200)}",
        "metroStation": 4,
        "phone": f"+7999{random.randint(1_000_000, 9_999_999)}",
        "rentTime": 3,
        "deliveryDate": (date.today() + timedelta(days=3)).isoformat(),
        "comment": f"Автотест {suffix}",
    }
    if color is not None:
        payload["color"] = color
    return payload
