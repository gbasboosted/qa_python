import allure

from api_client import OrderApi
from data import ResponseMessages, TestData


@allure.feature("Принятие заказа")
class TestAcceptOrder:
    @allure.title("Курьер может принять существующий заказ")
    def test_accept_order_returns_ok(self, registered_courier, created_order):
        response = OrderApi.accept(created_order["id"], registered_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Без id курьера заказ нельзя принять")
    def test_accept_order_without_courier_id_returns_error(self, created_order):
        response = OrderApi.accept(created_order["id"])

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": ResponseMessages.ORDER_DATA_MISSING,
        }

    @allure.title("Несуществующий курьер не может принять заказ")
    def test_accept_order_with_invalid_courier_id_returns_error(
        self,
        created_order,
    ):
        response = OrderApi.accept(created_order["id"], TestData.NONEXISTENT_ID)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.COURIER_ID_NOT_FOUND,
        }

    @allure.title("Запрос без id заказа возвращает ошибку")
    def test_accept_order_without_order_id_returns_error(self, registered_courier):
        response = OrderApi.accept("", registered_courier["id"])

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ROUTE_NOT_FOUND,
        }

    @allure.title("Запрос с неверным id заказа возвращает ошибку")
    def test_accept_order_with_invalid_order_id_returns_error(
        self,
        registered_courier,
    ):
        response = OrderApi.accept(
            TestData.NONEXISTENT_ID,
            registered_courier["id"],
        )

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ORDER_ID_NOT_FOUND,
        }
