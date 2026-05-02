import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

ORDER_ID = 5


@pytest.fixture
def create_order():
    payload = {
        "id": ORDER_ID,
        "petId": 99991,
        "quantity": 1,
        "status": "placed",
        "complete": False,
    }
    requests.post(f"{BASE_URL}/store/order", json=payload)
    yield
    requests.delete(f"{BASE_URL}/store/order/{ORDER_ID}")


def test_get_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_create_order():
    payload = {
        "id": ORDER_ID,
        "petId": 99991,
        "quantity": 2,
        "status": "placed",
        "complete": False,
    }
    response = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"


def test_get_order_by_id(create_order):
    response = requests.get(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == ORDER_ID


def test_delete_order(create_order):
    response = requests.delete(f"{BASE_URL}/store/order/{ORDER_ID}")
    assert response.status_code == 200
