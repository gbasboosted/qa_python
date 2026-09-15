import allure

from api_client import CourierApi
from data import ResponseMessages, TestData


@allure.feature("Удаление курьера")
class TestDeleteCourier:
    @allure.title("Курьера можно удалить")
    def test_delete_existing_courier_returns_ok(self, registered_courier):
        response = CourierApi.delete(registered_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Удаление без id возвращает ошибку")
    def test_delete_courier_without_id_returns_error(self):
        response = CourierApi.delete("")

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.ROUTE_NOT_FOUND,
        }

    @allure.title("Удаление по несуществующему id возвращает ошибку")
    def test_delete_nonexistent_courier_returns_error(self):
        response = CourierApi.delete(TestData.NONEXISTENT_ID)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": ResponseMessages.COURIER_NOT_FOUND,
        }
