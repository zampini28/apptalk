from flask import g, current_app
import click
import sqlite3
import os

sqlite3.register_converter("timestamp",
                           lambda x : datetime.fromisoformat(x.decode()))

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"],
                               detect_types = sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(_):
    db = g.pop("db", None)
    if db: db.close()

def init_db():
    db = get_db()
    for fn in [f for f in os.listdir("sql") if f.endswith(".sql")]:
        with current_app.open_resource(os.path.join("sql", fn)) as f:
            db.executescript(f.read().decode("utf8"))

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("the database was initialized")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
