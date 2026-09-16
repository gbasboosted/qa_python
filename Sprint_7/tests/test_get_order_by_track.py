import allure

from api_client import OrderApi
from data import ResponseMessages, TestData


@allure.feature("Получение заказа по номеру")
class TestGetOrderByTrack:
    @allure.title("По track возвращается объект созданного заказа")
    def test_get_order_by_track_returns_order(self, created_order):
        response = OrderApi.get_by_track(created_order["track"])

        assert response.status_code == 200
        assert isinstance(response.json().get("order"), dict)
        assert response.json()["order"]["track"] == created_order["track"]

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_get_order_without_track_returns_error(self):
        response = OrderApi.get_by_track()

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": ResponseMessages.ORDER_DATA_MISSING,
        }

    @allure.title("Несуществующий номер заказа возвращает ошибку")
    def test_get_order_with_invalid_track_returns_error(self):
        response = OrderApi.get_by_track(TestData.NONEXISTENT_ID)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ORDER_NOT_FOUND,
        }
