from main.controllers.user import *


def test_create_user_controller(client):
    response = client.post(
        "/users",
        json={
            "name": "Tracy",
            "email": "tracy@goitit.ai",
            "password": "dummy_password",
        },
    )
    assert response.status_code == 200
    response = client.post(
        "/users",
        json={
            "name": "Tracy",
            "email": "tracy@goitit.ai",
            "password": "dummy_password",
        },
    )
    assert response.status_code == 400


def test_get_user_controller(client):
    create_user(name="Joe", email="joe@joes.com", password="12345")
    response = client.post(
        "/login", json={"email": "joe@joes.com", "password": "12345"}
    )
    token = response.json["bearer"]
    assert token is not None
    response = client.get("/users/me", headers={"Authorization": token})
    assert response.status_code == 200


def test_login_user(client):
    create_user(name="Joe", email="joe@joes.com", password="12345")
    response = client.post("login", json={"email": "joe@joes.com", "password": "12345"})
    assert response.status_code == 200
    response = client.post(
        "login", json={"email": "joe@joes.com", "password": "abc12345"}
    )
    assert response.status_code == 500
