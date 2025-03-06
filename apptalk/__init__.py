from flask import Flask
import os, secrets
from . import routes, database as db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True,
                template_folder = os.path.join(os.getcwd(), "templates"),
                static_folder   = os.path.join(os.getcwd(), "static"))

    app.config.from_mapping(
        SECRET_KEY     = secrets.token_hex(),
        DATABASE       = os.path.join(app.instance_path, "apptalk.sqlite"),
        JWT_SECRET_KEY = secrets.token_hex(),
    )

    if test_config: app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route("/helloworld")
    def helloworld(): return "hello world"

    # esse caralho não funciona bp com 404, com outros funcionam
    # https://flask.palletsprojects.com/en/stable/errorhandling/#handling
    @app.errorhandler(404)
    def page_not_found(error): return "page not found"

    db.init_app(app)
    app.register_blueprint(routes.bp)
    return app
