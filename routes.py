from flask import render_template
from app import app

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
    return "Not Implemented", 501

@app.route("/conversa") # + /username
def chat():
    return "Not Implemented", 501

# TODO: add icon
#@app.route("/favicon.ico")
#def favicon():
#    return send_file("static/favicon.ico")



## api server

@app.route("/session", methods=["POST"])
def session():
    return "Not Implemented", 501
