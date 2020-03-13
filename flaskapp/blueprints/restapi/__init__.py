from flask import Blueprint, make_response, jsonify
from flaskapp.blueprints.restapi.singleton_api import SingletonApi
from .product_resource import ProductItemResource, ProductResource
from .auth_resource import RegisterAPI, LoginAPI, LogoutAPI, UserAPI, ToPostman

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = SingletonApi.get_instance()


@api.errorhandler(Exception)
def error_handler(e):
    message = 'Something is real bad, Details: {}'.format(str(e))
    print(message)
    return make_response(jsonify(message), 500)


def init_app(app):
    api.init_app(bp)
    api.add_resource(LoginAPI, "/login")
    api.add_resource(LogoutAPI, "/logout")

    api.add_resource(UserAPI, "/users/", "/users/<id>")

    api.add_resource(ProductResource, "/product/")
    api.add_resource(ProductItemResource, "/product/<product_id>")
    api.add_resource(ToPostman, "/postman")
    app.register_blueprint(bp)
