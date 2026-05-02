import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

USERNAME = "testuser_automation"


@pytest.fixture(autouse=True)
def create_user():
    payload = {
        "id": 0,
        "username": USERNAME,
        "firstName": "Test",
        "lastName": "User",
        "email": "test@automation.com",
        "password": "senha123",
        "phone": "81999999999",
        "userStatus": 1,
    }
    requests.post(f"{BASE_URL}/user", json=payload)
    yield
    requests.delete(f"{BASE_URL}/user/{USERNAME}")


def test_create_user():
    payload = {
        "id": 0,
        "username": USERNAME,
        "firstName": "Test",
        "lastName": "User",
        "email": "test@automation.com",
        "password": "senha123",
        "phone": "81999999999",
        "userStatus": 1,
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200


def test_get_user_by_username():
    response = requests.get(f"{BASE_URL}/user/{USERNAME}")
    assert response.status_code == 200
    assert response.json()["username"] == USERNAME


def test_update_user():
    payload = {
        "id": 0,
        "username": USERNAME,
        "firstName": "Updated",
        "lastName": "User",
        "email": "updated@automation.com",
        "password": "senha123",
        "phone": "81988888888",
        "userStatus": 1,
    }
    response = requests.put(f"{BASE_URL}/user/{USERNAME}", json=payload)
    assert response.status_code == 200


def test_login_user():
    response = requests.get(
        f"{BASE_URL}/user/login",
        params={"username": USERNAME, "password": "senha123"},
    )
    assert response.status_code == 200


def test_logout_user():
    response = requests.get(f"{BASE_URL}/user/logout")
    assert response.status_code == 200


def test_delete_user():
    response = requests.delete(f"{BASE_URL}/user/{USERNAME}")
    assert response.status_code in (200, 404)
