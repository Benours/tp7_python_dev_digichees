from fastapi.testclient import TestClient
import unittest
from src.main import app

client = TestClient(app)

def test_get_all_object():
    response = client.get("/object/all")
    assert response.status_code == 200

def test_get_object_by_id():
    response = client.get("/object/get/1")
    assert response.status_code == 404

def test_add_object():
    response = client.post("/object/add", json={
            "name": "test",
            "height": 1,
            "weight": 1,
            "description": "XXX",
            "price": 1,
            "stockline": 1,
            "shop": 1,
            "conditioning": 1
        })
    assert response.status_code, 200

def test_update_object():
    response = client.put("/object/update/9", json={
            "name": "test",
            "height": 1,
            "weight": 1,
            "description": "XXX",
            "price": 1,
            "stockline": 1,
            "shop": 1,
            "conditioning": 1
    })
    assert response.status_code, 200

def test_delete_object():
    response = client.delete("/object/del/10")
    assert response.status_code, 200

if __name__ == "__main__":
    unittest.main()