from flask import Blueprint
from flask_restful import Api
from .resources import RegisterAPI, LoginAPI, LogoutAPI, UserAPI

bp = Blueprint("authapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(RegisterAPI, "/auth/create")
    api.add_resource(LoginAPI, "/auth/login")
    api.add_resource(LogoutAPI, "/auth/logout")
    api.add_resource(UserAPI, "/auth/users", "/auth/users/<id>")
    app.register_blueprint(bp)

