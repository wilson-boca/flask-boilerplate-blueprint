from flask_restplus import Resource
from flaskapp.celery_ext.tasks import make_coffee
from flaskapp.models import User


class TestCelery(Resource):

    def get(self, name):
        make_coffee.delay(name)
        return 'Order received {}, check the terminal for your coffee...'.format(name)
