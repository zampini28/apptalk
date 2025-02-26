from flask import Flask
import os
import time
import secrets
from . import database as db
from . import routes

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True,
                template_folder = os.path.join(os.getcwd(), "templates"),
                static_folder   = os.path.join(os.getcwd(), "static"))

    app.config.from_mapping(
        SECRET_KEY = secrets.token_hex(),
        DATABASE   = os.path.join(app.instance_path, "apptalk.sqlite")
    )

    if test_config: app.config.update(test_config)

    try: os.makedirs(app.instance_path)
    except OSError: pass

    @app.route("/hello")
    def hello():
        return "hello - " + time.strftime("%Y-%m-%d %H:%M:%S")

    @app.route("/helloworld")
    def helloworld():
        return "hello world"

    # esse caralho não funciona bp com 404, com outros funcionam
    # https://flask.palletsprojects.com/en/stable/errorhandling/#handling
    @app.errorhandler(404)
    def page_not_found(error):
        return "page not found"

    db.init_app(app)
    app.register_blueprint(routes.bp)
    return app
