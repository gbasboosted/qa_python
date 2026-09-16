"""Фикстуры создают уникальные данные и очищают их после теста."""

import time

import pytest

from api_client import CourierApi, OrderApi
from helpers import generate_courier_payload, generate_order_payload


def get_order_id_when_available(track, attempts=5):
    for _ in range(attempts):
        response = OrderApi.get_by_track(track)
        order = response.json().get("order")
        if response.status_code == 200 and order:
            return order.get("id")
        time.sleep(1)
    return None


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
                courier_id = login_response.json().get("id")
                if courier_id is not None:
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
            track = response.json().get("track")
            if track is not None:
                created_tracks.append(track)

        return {"payload": payload, "response": response}

    yield create_order

    for track in reversed(created_tracks):
        OrderApi.cancel(track)


@pytest.fixture
def registered_courier(courier_factory):
    return courier_factory()


@pytest.fixture
def created_order(order_factory):
    order = order_factory(["BLACK"])
    response = order["response"]
    track = response.json().get("track") if response.status_code == 201 else None
    order["track"] = track
    order["id"] = get_order_id_when_available(track) if track else None
    return order
