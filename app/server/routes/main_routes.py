from flask import Blueprint
from app.server.extensions import db, factory

class MainRoutes:

    main = Blueprint('main', __name__)

    @main.route("/")
    @main.route("/home")
    def home():
        return "Hello World!"