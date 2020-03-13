from flask_restplus import Api


class SingletonApi(object):
    __instance = None
    __authorizations = {
        'Authorization': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Add Bearer before your token string',
            'example': 'Bearer TOKEN'
        }
    }

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Api(version='0.0.1', title='API Swagger-UI', description='A simple REST API example', authorizations=cls.__authorizations, ordered=True)
        return cls.__instance
