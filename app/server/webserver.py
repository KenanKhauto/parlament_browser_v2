import os

from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .routes.main_routes import MainRoutes
from .routes.raw_data_routes import RawDataRoutes
from .extensions import db, factory

class WebServer:
    def __init__(self):
        self._host = "localhost"
        self._port = 5000
        self._app = Flask(__name__)
        self._app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        self._login_manager = LoginManager()
        self._bcrypt = Bcrypt()
        self._login_manager.init_app(self._app)
        self._bcrypt.init_app(self._app)
        self._login_manager.login_view = "users.login"  # this is what we pass for @login_required
        self._login_manager.login_message_category = "info"
        self._db_connection = db
        self._factory = factory
        self._register_blueprints()

    def _register_blueprints(self):
        self._app.register_blueprint(MainRoutes.main)
        self._app.register_blueprint(RawDataRoutes.raw)

    def run(self):
        self._app.run(host=self._host, port=self._port, debug=True)

