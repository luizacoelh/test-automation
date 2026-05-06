import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

PET_ID = 99991


@pytest.fixture(autouse=True)
def create_pet():
    payload = {
        "id": PET_ID,
        "name": "Rex",
        "status": "available",
        "photoUrls": ["http://example.com/rex.jpg"],
    }
    requests.post(f"{BASE_URL}/pet", json=payload)
    yield
    requests.delete(f"{BASE_URL}/pet/{PET_ID}")


def test_create_pet():
    payload = {"id": PET_ID, "name": "Rex", "status": "available", "photoUrls": []}
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"


def test_get_pet_by_id():
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == PET_ID
    assert response.json()["status"] == "available"



def test_update_pet():
    payload = {"id": PET_ID, "name": "Rex Updated", "status": "sold", "photoUrls": []}
    response = requests.put(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex Updated"
    assert response.json()["status"] == "sold" 


def test_find_pets_by_status():
    response = requests.get(f"{BASE_URL}/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_pet():
    response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")
    assert response.status_code in (200, 404)
