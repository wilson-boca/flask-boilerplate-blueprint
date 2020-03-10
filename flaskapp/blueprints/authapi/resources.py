import datetime
from flask import request, make_response, jsonify, abort
from flask_jwt_extended import jwt_required, get_raw_jwt, create_access_token, create_refresh_token
from flask.views import MethodView
from flaskapp.ext.auth import add_to_black_list
from flaskapp.models import User
from flaskapp.ext.auth import check_hash, generate_hash


class RegisterAPI(MethodView):

    @jwt_required
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


class LoginAPI(MethodView):
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


class UserAPI(MethodView):

    def __query(self, args):
        users = [user.as_dict() for user in User.list_all()]
        return make_response(jsonify(users), 200)

    @jwt_required
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


class LogoutAPI(MethodView):

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
