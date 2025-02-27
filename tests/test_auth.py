import pytest
from flask import g
from flask import session

from apptalk.database import get_db

def test_register(client, app):
    assert client.get("/cadastro").status_code == 200

    response = client.post("/cadastro", data={
        "name": "a", "email": "a", "username": "a", "password": "a"
    })
    assert response.headers["Location"] == "/login"

    with app.app_context():
        assert (get_db() \
                .execute("SELECT * FROM users WHERE username = 'a'") \
                .fetchone()
                is not None)


def test_login(client, auth):
    assert client.get("/login").status_code == 200

    #response = auth.login("Alice123", "SuperSecretAlicePassword")
    #assert response.headers["Location"] == "/contatos"

    #response = auth.login("Bob456", "SuperSecretBobPassword")
    #assert response.headers["Location"] == "/contatos"


