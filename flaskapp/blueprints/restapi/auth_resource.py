import datetime
from flask import request, make_response, jsonify
from flask_jwt_extended import get_raw_jwt, create_access_token, jwt_required
from flask_restplus import fields, Resource
from flaskapp.ext.auth import add_to_black_list
from flaskapp.models import User
from flaskapp.ext.auth import check_hash, generate_hash
from flaskapp.blueprints.restapi.singleton_api import SingletonApi

api = SingletonApi.get_instance()

user = api.model('User', {
    'name': fields.String(example='Rodrigo'),
    'username': fields.String(example='rodrigo@gmail.com'),
    'password': fields.String(example='123456'),
    'profile': fields.String(example='user')
})


login = api.model('Login', {
    'username': fields.String(description='Your username', example='wilson2@gmail.com'),
    'password': fields.String(description='Your password', example='123456')
})


class RegisterAPI(Resource):
    @api.doc(security='Authorization')
    @api.expect(user)
    def post(self):
        try:
            post_data = request.get_json()
            post_data['password'] = generate_hash(post_data.get('password', ''))
            user = User.create_from_dict(post_data)
            return make_response(jsonify(user.as_dict()), 201)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
            }
            return make_response(jsonify(response_object), 500)


class LoginAPI(Resource):

    @api.expect(login)
    def post(self):
        try:
            post_data = request.get_json()
            user = User.filter_by(username=post_data.get('username')).first()
            if check_hash(user.password, post_data.get('password', '')):
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'token': create_access_token(identity=user.as_dict())
                }
                return make_response(jsonify(response_object), 200)
            response_object = {
                'status': 'fail',
                'message': 'Invald password.'
            }
            return make_response(jsonify(response_object), 404)
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again, detlais: {}'.format(str(e))
            }
            return make_response(jsonify(response_object), 500)


class UserAPI(Resource):

    def __query(self, args):
        users = [user.as_dict() for user in User.list_all()]
        return make_response(jsonify(users), 200)

    @jwt_required
    @api.doc(security='Authorization')
    def get(self, id=None):
        try:
            if id is None:
                return self.__query({})
            return make_response(jsonify(User.get(id).as_dict()))
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again, detlais: {}'.format(str(e))
            }
            return make_response(jsonify(response_object), 500)

    @api.doc(security='Authorization')
    def post(self):
        try:
            post_data = request.get_json()
            post_data['password'] = generate_hash(post_data.get('password', ''))
            user = User.create_from_dict(post_data)
            return make_response(jsonify(user.as_dict()), 201)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.',
            }
            return make_response(jsonify(response_object), 500)


class LogoutAPI(Resource):

    @jwt_required
    def post(self):
        try:
            jti = get_raw_jwt()['jti']
            add_to_black_list(jti)
            response_object = {
                'status': 'success',
                'message': 'Successfully logged out.',
                'token': create_access_token(identity='Logout', expires_delta=datetime.timedelta(days=0, seconds=1))
            }
            return make_response(jsonify(response_object), 200)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': str(e)
            }
            return make_response(jsonify(response_object), 500)


class ToPostman(Resource):

    @jwt_required
    def get(self):
        try:
            return make_response(jsonify(api.as_postman(urlvars=False, swagger=True)), 200)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': str(e)
            }
            return make_response(jsonify(response_object), 500)
