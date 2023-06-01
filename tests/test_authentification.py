from fastapi.testclient import TestClient
import unittest
from src.main import app
import json

# TODO test to see if empty or partial formular return 400. also unrestristation while no co (and logout)

#Client used to test the differents fonctionalities of the app.
clientTest = TestClient(app)


#Test to see if a bad email return a status 400.
def test_login_KO_bad_email():
    response = clientTest.post("/authentification/login", json={
        "email": "bad_mail@gmail.com",
        "password": "bad_password"
    })
    assert response.status_code == 400


#Test to see if a bad email and a bad password return a status 400.
def test_login_KO_bad_email_bad_password():
    response = clientTest.post("/authentification/login", json={
        "email": "bad_mail@gmail.com",
        "password": "bad_password"
    })
    assert response.status_code == 400


#Test to see if a good email and a bad password return a status 400.
def test_login_KO_bad_password():
    response = clientTest.post("/authentification/login", json={
        "email": "mikael.ledevehat@gmail.com",
        "password": "bad_password"
    })
    assert response.status_code == 400


#Test to see if a good email and a good password return a status 200, with a valid token.
def test_login():
    response = clientTest.post("/authentification/login", json={
        "email": "mikael.ledevehat@gmail.com",
        "password": "truc"
    })

    assert response.status_code == 200
    jsonResponse = json.loads(response.text)
    assert jsonResponse["token"] == "1d-Dqb0V3328LU2YYjoT8w"


#Test to see if a logout with a bad token return a status 400.
def test_logout_KO_bad_token():
    response = clientTest.post("/authentification/logout", json={
       "token":"bad_token"
    })

    assert response.status_code == 400


#Test to see if a logout with a good token return status 200.
def test_logout():
    response = clientTest.post("/authentification/logout", json={
       "token":"1d-Dqb0V3328LU2YYjoT8w"
    })

    assert response.status_code == 200


#Test to see if a logout with a good token while not connected first return a status 400.
def test_logout_KO_unconnected():
    response = clientTest.post("/authentification/logout", json={
       "token":"1d-Dqb0V3328LU2YYjoT8w"
    })

    assert response.status_code == 400


#Test to see if a registration with an already used email return a status 400.
def test_register_KO_used_email_v1():
    response = clientTest.post("/authentification/register", json={
        "email": "mikael.ledevehat@gmail.com",
        "password": "truc",
        "first_name": "Mikael",
        "last_name": "Le Devehat",
    })
    assert response.status_code == 400


#Test to see if a registration with unique email return a status 200.
def test_register():
    response = clientTest.post("/authentification/register", json={
        "email": "mikael6.ledevehat@gmail.com",
        "password": "truc",
        "first_name": "Mikael",
        "last_name": "Le Devehat",
    })
    assert response.status_code == 200


#Test to see if same registration with same email still return a status 400.
def test_register_KO_used_email_v2():
    response = clientTest.post("/authentification/register", json={
        "email": "mikael6.ledevehat@gmail.com",
        "password": "truc",
        "first_name": "Mikael",
        "last_name": "Le Devehat",
    })
    assert response.status_code == 400


#Test to see if an unregistration with a bad token return a status 400.
def test_unregister_KO_bad_token():
    response = clientTest.post("/authentification/unregister", json={
        "token": "bad_token",
    })
    assert response.status_code == 400


#Test to see if an unregistration with a good token and a connected user return a status 200.
def test_unregister():
    response = clientTest.post("/authentification/login", json={
        "email": "mikael6.ledevehat@gmail.com",
        "password": "truc"
    })

    jsonResponse = json.loads(response.text)

    response = clientTest.post("/authentification/unregister", json={
        "token" : jsonResponse["token"]
    })

    assert response.status_code == 200


def test_unregister_KO_unconnected():
    response = clientTest.post("/authentification/register", json={
        "email": "mikael6.ledevehat@gmail.com",
        "password": "truc",
        "first_name": "Mikael",
        "last_name": "Le Devehat",
    })
    assert response.status_code == 200

    response = clientTest.post("/authentification/login", json={
        "email": "mikael6.ledevehat@gmail.com",
        "password": "truc"
    })

    assert response.status_code == 200
    jsonResponse = json.loads(response.text)
    assert jsonResponse["token"] == "1d-Dqb0V3328LU2YYjoT8w"

    response = clientTest.post("/authentification/logout", json={
        "token": "1d-Dqb0V3328LU2YYjoT8w"
    })

    assert response.status_code == 200

    response = clientTest.post("/authentification/unregister", json={
        "token" : jsonResponse["token"]
    })

    assert response.status_code == 200


if __name__ == "__main__":
    unittest.main()