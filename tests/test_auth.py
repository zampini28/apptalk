import pytest
from apptalk.database import get_db

@pytest.mark.parametrize(
    ("name", "email", "username", "password"),
    (("Alice", "alice@example.com", "Alice123", "SuperSecretAlicePassword"),
     ("Bob", "Bob@example.com", "Bob456", "SuperSecretBobPassword"))
)
def test_register(client, auth, app, name, email, username, password):
    assert client.get("/cadastro").status_code == 200

    response = auth.register(name, email, username, password)

    assert response.status_code == 302
    assert response.headers["Location"] == "/login"

    with app.app_context():
        user = (get_db()
                .execute("SELECT * FROM users WHERE username = ?", (username,))
                .fetchone())
        assert user and user["password"] != password

@pytest.mark.parametrize(
    ("username", "password"),
    (("Alice123", "SuperSecretAlicePassword"),
     ("Bob456", "SuperSecretBobPassword"))
)
def test_login(client, auth, username, password):
    assert client.get("/login").status_code == 200

    response = auth.login(username, password)

    assert response.status_code == 302
    assert response.headers["Location"] == "/contatos"


