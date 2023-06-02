from fastapi.testclient import TestClient
import unittest
from src.main import app

client = TestClient(app)

# Test to get all weights
def test_get_all_weights():
    response = client.get("/weight/all")
    assert response.status_code == 200

# Test to get one weight
def test_get_weight_by_id():
    response = client.get("/weight/get/3")
    assert response.status_code == 404

# Test to add weight
def test_add_weight():
    response = client.post("/weight/add", json={
            "w_val": 1
        })
    assert response.status_code, 200

# Test to update weight
def test_update_weight():
    response = client.put("/weight/update/3", json={
            "w_val": 1
    })
    assert response.status_code, 200

# Test to delete weight
def test_delete_weight():
    response = client.delete("/weight/del/3")
    assert response.status_code, 200

if __name__ == "__main__":
    unittest.main()