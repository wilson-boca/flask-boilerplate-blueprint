from flask_restplus import Resource
from flaskapp.celery_ext.tasks import make_coffee, make_capuccino
from flaskapp.models import User


class MakeQuickCoffee(Resource):

    def get(self, name):
        make_coffee.delay(name)
        return 'Order received {}, check the terminal for your coffee...'.format(name)


class MakeSlowCapuccino(Resource):

    def get(self, name):
        make_capuccino.delay(name)
        return 'Order received {}, check the terminal for your slow capuccino...'.format(name)
