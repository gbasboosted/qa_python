import allure
import pytest

from api_client import CourierApi
from data import ResponseMessages
from helpers import generate_courier_payload


@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьера можно создать")
    def test_create_courier_returns_ok(self, courier_factory):
        courier = courier_factory()

        assert courier["response"].status_code == 201
        assert courier["response"].json() == {"ok": True}

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_duplicate_courier_returns_conflict(self, courier_factory):
        courier = courier_factory()
        duplicate_response = CourierApi.create(courier["payload"])

        assert duplicate_response.status_code == 409
        assert duplicate_response.json() == {
            "code": 409,
            "message": ResponseMessages.LOGIN_ALREADY_USED,
        }

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Без обязательного поля {missing_field} курьер не создаётся")
    def test_create_courier_without_required_field_returns_error(
        self,
        missing_field,
    ):
        payload = generate_courier_payload()
        payload.pop(missing_field)

        response = CourierApi.create(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": ResponseMessages.COURIER_DATA_MISSING,
        }
