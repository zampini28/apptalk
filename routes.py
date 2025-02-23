from flask import render_template, request, redirect, url_for, flash, session, g
from app import app
from database import get_connection
import sqlite3
import uuid

app.secret_key = str(uuid.uuid4())

## web server
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def signup():
    return render_template("signup.html")

@app.route("/contatos")
def contacts():
    return render_template("contacts.html")

@app.route("/conversa/<username>")
def chat(username):
    return render_template("chat.html", username=username)

@app.errorhandler(404)
def page_not_found():
    return "Page not found", 404

@app.errorhandler(500)
def internal_error():
    return "Internal Error", 500

@app.errorhandler(501)
def not_implemented():
    return "Not Implemented", 501

## api server
@app.route("/session", methods=["POST"])
def session_route():
    action   = request.form.get("action")
    name     = request.form.get("name")
    email    = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    if action == "signup":
        if register_user(name, email, username, password):
            return redirect(url_for("contacts"))
        else:
            return redirect(url_for("signup"))

    elif action == "login":
        if validate_login(username, password):
            session['user'] = username
            return redirect(url_for("contacts"))
        else:
            flash("Invalid credentials", "failed")
            return redirect(url_for("login"))

    return internal_error()

def register_user(name, email, username, password):
    con, cur = get_connection()

    try:
        cur.execute("""INSERT INTO users (name, email, username, password)
                       VALUES (?,?,?,?)""", (name, email, username, password,))
        con.commit()
        return True

    except sqlite3.IntegrityError:
        flash("Username already exists", "failed")

    except sqlite3.Error as e:
        flash(f"Error during signup: {e}", "failed")

    con.close()
    return False


def validate_login(username, password):
    con, cur = get_connection()
    try:
        cur.execute("""SELECT username FROM users WHERE username = ? AND password = ?""", (username, password))
        return bool(cur.fetchone())

    except sqlite3.Error as e:
        flash(f"Error during login: {e}", "failed")

    finally:
        con.close()
    return False

@app.before_request
def load_user():
    if 'user' in session:
        g.user = session['user']
    else:
        g.user = None

@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("home"))
