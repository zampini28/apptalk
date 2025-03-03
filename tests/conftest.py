import os, tempfile, pytest
from apptalk import create_app
from apptalk.database import get_db, init_db

@pytest.fixture(scope="module")
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})

    with app.app_context(): init_db()
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username="test", password="test"):
        return self._client.post(
            "/login", data={"username": username, "password": password}
        )

    def register(self, name="test", email="test@example.com",
                    username="test", password="test"):
        return self._client.post(
            "/cadastro", data={"name": name, "email": email,
                               "username": username, "password": password}
        )

@pytest.fixture
def auth(client):
    return AuthActions(client)
