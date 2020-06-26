import werkzeug

from flask import Flask
from flaskapp.ext import configuration
from flaskapp.celery_ext.celery_utils import init_celery
from flaskapp import celery

werkzeug.cached_property = werkzeug.utils.cached_property


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app


def create_flask_celery_app(**config):
    app = create_app(**config)
    init_celery(celery, app)
    return app
