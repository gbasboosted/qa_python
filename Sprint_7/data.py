"""Тестовые данные и ожидаемые сообщения API."""


class ResponseMessages:
    COURIER_DATA_MISSING = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_USED = "Этот логин уже используется. Попробуйте другой."
    LOGIN_DATA_MISSING = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    COURIER_NOT_FOUND = "Курьера с таким id нет."
    COURIER_ID_NOT_FOUND = "Курьера с таким id не существует"
    ORDER_DATA_MISSING = "Недостаточно данных для поиска"
    ORDER_ID_NOT_FOUND = "Заказа с таким id не существует"
    ORDER_NOT_FOUND = "Заказ не найден"
    ROUTE_NOT_FOUND = "Not Found."


class TestData:
    NONEXISTENT_ID = 999_999_999
