import allure
import pytest

from api_client import CourierApi
from data import ResponseMessages
from helpers import generate_random_string


@allure.feature("Логин курьера")
class TestLoginCourier:
    @allure.title("Курьер может авторизоваться и получает id")
    def test_login_registered_courier_returns_id(self, registered_courier):
        payload = registered_courier["payload"]

        response = CourierApi.login(
            {"login": payload["login"], "password": payload["password"]}
        )

        assert response.status_code == 200
        assert isinstance(response.json().get("id"), int)
        assert response.json()["id"] == registered_courier["id"]

    @allure.title("Без логина авторизация возвращает ошибку")
    def test_login_without_login_returns_error(self):
        response = CourierApi.login({"password": generate_random_string()})

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": ResponseMessages.LOGIN_DATA_MISSING,
        }

    @allure.title("С пустым паролем авторизация возвращает ошибку")
    def test_login_with_empty_password_returns_error(self, registered_courier):
        response = CourierApi.login(
            {
                "login": registered_courier["payload"]["login"],
                "password": "",
            }
        )

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": ResponseMessages.LOGIN_DATA_MISSING,
        }

    @pytest.mark.parametrize("incorrect_field", ["login", "password"])
    @allure.title("Неверное поле {incorrect_field} возвращает ошибку")
    def test_login_with_incorrect_credentials_returns_error(
        self,
        registered_courier,
        incorrect_field,
    ):
        courier = registered_courier["payload"]
        payload = {
            "login": courier["login"],
            "password": courier["password"],
        }
        payload[incorrect_field] = generate_random_string(20)

        response = CourierApi.login(payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ACCOUNT_NOT_FOUND,
        }

    @allure.title("Несуществующий курьер не может авторизоваться")
    def test_login_nonexistent_courier_returns_not_found(self):
        response = CourierApi.login(
            {
                "login": generate_random_string(20),
                "password": generate_random_string(20),
            }
        )

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ACCOUNT_NOT_FOUND,
        }
