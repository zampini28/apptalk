from flask import Flask
import os
import time
import secrets
from . import database as db
from . import routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        host       = "0.0.0.0",
        port       = 6000,
        SECRET_KEY = secrets.token_hex(),
        DATABASE   = os.path.join(app.instance_path, "apptalk.sqlite")
    )

    try: os.makedirs(app.instance_path)
    except OSError: pass

    @app.route("/helloworld")
    def helloworld():
        return "hello world - " + time.strftime("%Y-%m-%d %H:%M:%S")

    # esse caralho não funciona bp com 404, com outros funcionam
    # https://flask.palletsprojects.com/en/stable/errorhandling/#handling
    @app.errorhandler(404)
    def page_not_found(error):
        return "page not found"

    db.init_app(app)
    app.register_blueprint(routes.bp)
    return app
