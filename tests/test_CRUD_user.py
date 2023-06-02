from fastapi.testclient import TestClient
import unittest
from src.main import app

client = TestClient(app)

# Test to get all users
def test_get_all_users():
    response = client.get("/user/all")
    assert response.status_code == 200

# Test to get one user
def test_get_user_by_id():
    response = client.get("/user/get/1")
    assert response.status_code == 404

# Test to add user
def test_add_user():
    response = client.post("/user/add", json={
            "email": "test@example.com",
            "password": "password",
            "firstname": "John",
            "lastname": "Doe"
        })
    assert response.status_code, 200

# Test to update user
def test_update_user():
    response = client.put("/user/update/1", json={
        "email": "updated@example.com",
        "password": "newpassword"
    })
    assert response.status_code, 200

# Test to delete user
def test_delete_user():
    response = client.delete("/user/del/1")
    assert response.status_code, 200

if __name__ == "__main__":
    unittest.main()