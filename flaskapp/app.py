from flask import Flask
import werkzeug
from flaskapp.ext import configuration

werkzeug.cached_property = werkzeug.utils.cached_property


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app
