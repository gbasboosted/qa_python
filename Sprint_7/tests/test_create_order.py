import allure
import pytest


@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize(
        "color",
        (["BLACK"], ["GREY"], ["BLACK", "GREY"], None),
        ids=("black", "grey", "both_colors", "without_color"),
    )
    @allure.title("Заказ создаётся с вариантом цвета: {param_id}")
    def test_create_order_with_different_colors_returns_track(
        self,
        order_factory,
        color,
    ):
        order = order_factory(color)
        response = order["response"]

        assert response.status_code == 201
        assert isinstance(response.json().get("track"), int)
