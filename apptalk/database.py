from flask import g, current_app
from datetime import datetime
import click, sqlite3, os

sqlite3.register_converter("timestamp",
                           lambda x : datetime.fromisoformat(x.decode()))

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"],
                               detect_types = sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(_):
    if (db := g.pop("db", None)): db.close()

def init_db():
    db, sql_dir = get_db(), os.path.abspath(os.path.join(os.getcwd(), "sql"))
    for fn in filter(lambda f: f.endswith(".sql"), os.listdir(sql_dir)):
        with current_app.open_resource(os.path.join(sql_dir, fn)) as f:
            db.executescript(f.read().decode("utf8"))

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("the database was initialized")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
