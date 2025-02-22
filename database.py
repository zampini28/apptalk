import sqlite3
import os

# TODO: change it to an env var.
#TODO: Test for a server
DATABASE = "database.db"

def get_connection(database = DATABASE):
    con = sqlite3.connect(database, check_same_thread=False)
    con.row_factory = sqlite3.Row
    return con, con.cursor()

def init_database():
    con, cur = get_connection()
    for f in [f for f in os.listdir() if f.endswith(".sql")]:
        with open(f, "r") as x:
            s=x.read()
        try: con.executescript(s)
        except sqlite3.Error as e:
            print(f"error when reading {f}: {e}")
        con.commit()
        con.close()
