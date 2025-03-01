import pytest
from flask import g
from flask import session

from apptalk.database import get_db

@pytest.mark.parametrize(
    ("name", "email", "username", "password"),
    (("Alice", "alice@example.com", "Alice123", "SuperSecretAlicePassword"),
     ("Bob", "Bob@example.com", "Bob456", "SuperSecretBobPassword"))
)

def test_register(client, auth, app, name, email, username, password):
    assert client.get("/cadastro").status_code == 200

    response = auth.register(name, email, username, password)
    assert response.headers["Location"] == "/login"

    with app.app_context():
        assert (get_db()
                .execute(f"SELECT * FROM users WHERE username = '{username}'")
                .fetchone())

def test_login(client, auth):
    assert client.get("/login").status_code == 200

    #response = auth.login("Alice123", "SuperSecretAlicePassword")
    #assert response.headers["Location"] == "/contatos"

    #response = auth.login("Bob456", "SuperSecretBobPassword")
    #assert response.headers["Location"] == "/contatos"


