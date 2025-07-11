from fastapi.testclient import TestClient
from app.main import app
from faker import Faker
import pytest


client = TestClient(app)
faker = Faker()


@pytest.fixture
def new_data():
    return {"name": faker.name(), "descriptions": faker.name(), "is_active": True}



class TestSpecialties:

    url = "/api/specialties/"


    @pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"name": "Cardiology", "descriptions": "Heart specialist", "is_active": True}, 201),
        ({"name": "Neurology", "descriptions": "Brain and nerves", "is_active": False}, 201),
        ({"descriptions": "Missing name field", "is_active": True}, 422),
        ({}, 422),
    ]
    )
    def test_create_specialty_parametrize(self, payload,expected_status):
        response = client.post(self.url, json=payload)

        assert response.status_code == expected_status
        assert response.json()["name"] == payload["name"]
        assert response.json()["descriptions"] == payload["descriptions"]
        assert response.json()["is_active"] == payload["is_active"]
        assert not response.json()["name"] == "jalberth"


    def test_create_specialty(self, new_data):
        response = client.post(self.url, json=new_data)

        assert response.status_code == 201
        assert response.json()["name"] == new_data["name"]
        assert response.json()["descriptions"] == new_data["descriptions"]
        assert response.json()["is_active"] == new_data["is_active"]
        assert not response.json()["name"] == "jalberth"

    def test_create_specialties_missing_name(self):
        incomplete_data = {"descriptions": faker.name()}
        response = client.post(self.url, json=incomplete_data)
        assert response.status_code == 422

    def test_get_specialties(self):
        data = client.get(self.url)
        assert data.status_code == 200
        assert isinstance(data.json(), list)

    def test_get_specialty(self, new_data):
        post_response = client.post(self.url, json=new_data)
        assert post_response.status_code == 201

        created_id = post_response.json()["id"]
        get_response = client.get(f"{self.url}{created_id}")
        assert get_response.status_code == 200
        assert get_response.json()["name"] == new_data["name"]
        assert get_response.json()["descriptions"] == new_data["descriptions"]
        assert get_response.json()["is_active"] == new_data["is_active"]

    def test_put_specialties(self, new_data):
        post_response = client.post(self.url, json=new_data)
        assert post_response.status_code == 201
        created_id = post_response.json()["id"]

        update_data = {
            "name": faker.name(),
            "descriptions": faker.name(),
            "is_active": True,
        }
        response = client.put(f"{self.url}{created_id}", json=update_data)
        assert response.status_code == 200
        assert response.json()["name"] == update_data["name"]

    def test_put_missing_data(self, new_data):
        post_response = client.post(self.url, json=new_data)
        assert post_response.status_code == 201
        created_id = post_response.json()["id"]

        incomplete_data = {"descriptions": faker.name(), "is_active": True}
        response = client.put(f"{self.url}{created_id}", json=incomplete_data)
        assert response.status_code == 422

    def test_patch_specialties(self, new_data):
        post_response = client.post(self.url, json=new_data)
        assert post_response.status_code == 201
        created_id = post_response.json()["id"]

        patch_data = {"name": faker.name()}
        response = client.patch(f"{self.url}{created_id}", json=patch_data)
        assert response.status_code == 200
        assert response.json()["name"] == patch_data["name"]

    def test_delete_specialties(self, new_data):
        post_response = client.post(self.url, json=new_data)
        assert post_response.status_code == 201
        created_id = post_response.json()["id"]

        response = client.delete(f"{self.url}{created_id}")
        assert response.status_code == 200