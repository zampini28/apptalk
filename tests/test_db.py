import sqlite3, pytest
from apptalk.database import get_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)

def test_init_db_command(runner, monkeypatch):
    class Recorder:
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("apptalk.database.init_db", fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "the database was initialized" in result.output
    assert Recorder.called
