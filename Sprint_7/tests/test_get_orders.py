import allure

from api_client import OrderApi


@allure.feature("Список заказов")
class TestGetOrders:
    @allure.title("Ответ содержит список заказов")
    def test_get_orders_returns_orders_list(self):
        response = OrderApi.get_list({"limit": 1, "page": 0})

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
