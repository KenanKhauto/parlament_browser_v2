import os

from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from .routes.main_routes import MainRoutes
from .routes.raw_data_routes import RawDataRoutes
from .extensions import db, factory

class WebServer:
    """
    A web server class built using Flask to manage and serve web content.
    
    @ivar _host: The host address for the server. Default is "localhost".
    @ivar _port: The port number on which the server listens. Default is 5000.
    @ivar _app: The Flask application instance.
    @ivar _login_manager: Manager for user login functionality.
    @ivar _bcrypt: Bcrypt instance for password hashing.
    @ivar _db_connection: Database connection instance.
    @ivar _factory: An instance related to the application's factory configuration.
    """

    def __init__(self):
        """
        Initializes the WebServer with default configurations and attributes.
        """
        self._host = "localhost"
        self._port = 5000
        self._app = Flask(__name__)
        CORS(self._app)
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
        """
        Registers the blueprints (modules) for the Flask application.
        
        Currently, it registers MainRoutes and RawDataRoutes.
        """
        self._app.register_blueprint(MainRoutes.main)
        self._app.register_blueprint(RawDataRoutes.raw)

    def run(self):
        """
        Runs the Flask application with the specified host and port.
        
        By default, it uses debug mode for development purposes.
        """
        self._app.run(host=self._host, port=self._port, debug=True)

