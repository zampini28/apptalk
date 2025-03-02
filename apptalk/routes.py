from flask import Blueprint, render_template, request, redirect, url_for, flash
from .database import get_db
from .encryption import hashpw, checkpw
from uuid import uuid4

bp = Blueprint("main", __name__)

SQL_INSERT_USER = \
"INSERT INTO users(id, name, email, username, password) VALUES (?,?,?,?,?)"

SQL_SELECT_USER = \
"SELECT * FROM users WHERE username = ?"

@bp.route("/")
def home(): return render_template("index.html")

@bp.route("/cadastro", methods=("GET", "POST"))
def signup():
    if request.method == "POST":
        fields_names = ("name", "email", "username", "password")
        fields = {k: request.form[k] for k in fields_names}

        if not all(fields.values()): flash("Todos os campos são obrigatórios.")
        else:
            db = get_db()
            try:
                username, password = fields["username"], fields["password"]
                fields["password"] = hashpw(username, password)
                db.execute(SQL_INSERT_USER, (str(uuid4()), *fields.values()))
                db.commit()
                return redirect(url_for("main.login"))
            except db.IntegrityError as e:
                flash(f"Usuário {fields['username']} já está registrado!")
    return render_template("signup.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username, password = request.form["username"], request.form["password"]
        if not all((username, password)):
            flash("Todos os campos são obrigatórios.")
        user = get_db().execute(SQL_SELECT_USER, (username,)).fetchone()
        if not user or not checkpw(user["password"], username, password):
            flash("Usuário e/ou senha estão incorretos.")
        else: return redirect(url_for("main.contacts"))
    return render_template("login.html")


@bp.route("/contatos")
def contacts(): return render_template("contacts.html")
