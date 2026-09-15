"""Фикстуры создают уникальные данные и очищают их после теста."""

import pytest

from api_client import CourierApi, OrderApi
from helpers import generate_courier_payload, generate_order_payload


@pytest.fixture
def courier_factory():
    created_courier_ids = []

    def create_courier(payload=None):
        courier = payload or generate_courier_payload()
        create_response = CourierApi.create(courier)
        courier_id = None

        if create_response.status_code == 201:
            login_response = CourierApi.login(
                {
                    "login": courier["login"],
                    "password": courier["password"],
                }
            )
            if login_response.status_code == 200:
                courier_id = login_response.json()["id"]
                created_courier_ids.append(courier_id)

        return {
            "payload": courier,
            "response": create_response,
            "id": courier_id,
        }

    yield create_courier

    for courier_id in reversed(created_courier_ids):
        CourierApi.delete(courier_id)


@pytest.fixture
def order_factory():
    created_tracks = []

    def create_order(color=None):
        payload = generate_order_payload(color)
        response = OrderApi.create(payload)

        if response.status_code == 201:
            created_tracks.append(response.json()["track"])

        return {"payload": payload, "response": response}

    yield create_order

    for track in reversed(created_tracks):
        OrderApi.cancel(track)


@pytest.fixture
def registered_courier(courier_factory):
    courier = courier_factory()
    assert courier["response"].status_code == 201
    assert courier["id"] is not None
    return courier


@pytest.fixture
def created_order(order_factory):
    order = order_factory(["BLACK"])
    assert order["response"].status_code == 201
    track = order["response"].json()["track"]
    get_response = OrderApi.get_by_track(track)
    assert get_response.status_code == 200
    order["track"] = track
    order["id"] = get_response.json()["order"]["id"]
    return order
