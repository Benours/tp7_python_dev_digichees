from fastapi.testclient import TestClient
import unittest
from src.main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/user/all")
    assert response.status_code == 200

def test_get_user_by_id():
    response = client.get("/user/1")
    assert response.status_code == 404

def test_add_user():
    response = client.post("/user/add", json={
            "email": "test@example.com",
            "password": "password",
            "firstname": "John",
            "lastname": "Doe"
        })
    assert response.status_code, 200

def test_update_user():
    response = client.put("/users/1", json={
        "email": "updated@example.com",
        "password": "newpassword"
    })
    assert response.status_code, 200

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code, 200

if __name__ == "__main__":
    unittest.main()