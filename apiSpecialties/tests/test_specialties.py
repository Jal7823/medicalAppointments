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
        ],
        ids=["valid_active", "valid_inactive", "missing_name", "empty_payload"]
    )
    def test_create_specialty_parametrize(self, payload, expected_status):
        response = client.post(self.url, json=payload)
        assert response.status_code == expected_status, f"Failed with payload: {payload}"

        if expected_status == 201:
            assert response.json()["name"] == payload["name"]
            assert response.json()["descriptions"] == payload["descriptions"]
            assert response.json()["is_active"] == payload["is_active"]
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

    @pytest.mark.parametrize(
        "payload, expected_status",
        [
            ({"name": "Cardiology", "descriptions": "Heart specialist", "is_active": True}, 200),
            ({"name": "Neurology", "descriptions": "Brain and nerves", "is_active": False}, 200),
        ],
        ids=["update_cardiology", "update_neurology"]
    )
    def test_put_specialties(self, payload, expected_status):
        post_response = client.post(self.url, json=payload)
        assert post_response.status_code == 201, f"Setup POST failed with payload: {payload}"
        created_id = post_response.json()["id"]

        response = client.put(f"{self.url}{created_id}", json=payload)
        assert response.status_code == expected_status, f"PUT failed with payload: {payload}"
        assert response.json()["name"] == payload["name"]

    @pytest.mark.parametrize(
        "payload",
        [
            {"descriptions": "Missing name", "is_active": True},
            {},
        ],
        ids=["missing_name", "empty_payload"]
    )
    def test_put_specialties_invalid(self, payload):
        post_response = client.post(self.url, json={
            "name": faker.name(),
            "descriptions": faker.name(),
            "is_active": True
        })
        assert post_response.status_code == 201
        created_id = post_response.json()["id"]

        response = client.put(f"{self.url}{created_id}", json=payload)
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

      
