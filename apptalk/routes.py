from flask import (
    Blueprint, render_template, request, redirect, url_for, flash
)
from .database import get_db
from uuid import uuid4

bp = Blueprint('main', __name__)

SQL_INSERT_USER = \
"INSERT INTO users(id, name, email, username, password) VALUES (?,?,?,?,?)"

SQL_SELECT_USER = \
"SELECT * FROM users WHERE username = ?"

@bp.route("/")
def home():
    return render_template("index.html")

@bp.route("/cadastro", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        name     = request.form["name"]
        email    = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        db, err = get_db(), None

        if not name:       err = "name is required"
        elif not email:    err = "email is required"
        elif not username: err = "username is required"
        elif not password: err = "password is required"

        if not err:
            try:
                db.execute(SQL_INSERT_USER,
                           (str(uuid4()), name, email, username, password,))
                db.commit()
            except db.IntegrityError as e:
                err = f"user {username} is already registered {e}"
            else:
                return redirect(url_for("main.login"))
        flash(err)
    return render_template("signup.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db, err = get_db(), None

        user = db.execute(SQL_SELECT_USER, (username,)).fetchone()

        if not user or user["password"] != password:
            err = "incorrect username or password"

        if not err:
            return redirect(url_for("main.contacts"))

        flash(err)
    return render_template("login.html")


@bp.route("/contatos")
def contacts():
    return render_template("contacts.html")
