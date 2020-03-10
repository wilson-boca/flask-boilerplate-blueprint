import secrets
from flask_simplelogin import SimpleLogin
from flask_jwt_extended import JWTManager
from werkzeug.security import check_password_hash, generate_password_hash
from flaskapp.models import User
from flaskapp.ext.database import db


def check_hash(hashed_password, password):
    return check_password_hash(hashed_password, password)


def generate_hash(password):
    return generate_password_hash(password)


def create_user(username, password):
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} is already on DB')
    user = User(username=username, password=generate_password_hash(password), profile='admin', name='AdminUser')
    db.session.add(user)
    db.session.commit()
    return user


def add_to_black_list(jti):
    blacklist.add(jti)


def verify_login(user):
    username = user.get('username')
    password = user.get('password')
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if existing_user.profile != 'admin':
        return False
    if check_password_hash(existing_user.password, password):
        return True
    return False


jwt = JWTManager()
blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


def init_app(app):
    app.config['SECRET_KEY'] = secrets.token_hex(32)
    jwt.init_app(app)
    SimpleLogin(app, login_checker=verify_login)
