from flaskapp import celery
from flaskapp.app import create_flask_celery_app
from flaskapp.celery_ext.celery_utils import init_celery

app = create_flask_celery_app()
init_celery(celery, app)
