import datetime
from flaskapp.ext.database import db
from flaskapp.abstract_model import AbstractModel


class Product(AbstractModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


class User(AbstractModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    username = db.Column(db.String(255), nullable=False, unique=True, index=True)
    profile = db.Column(db.String, nullable=False, default='user')
    password = db.Column(db.String)
    password_reset = db.Column(db.Boolean, default=True)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime)

    def as_dict(self, compact=True):
        if compact:
            return {
                "id": self.id,
                "username": self.username
            }
        return {
            "id": self.id,
            "username": self.username,
            "profile": self.profile,
            "active": self.active,
            "password_reset": self.password_reset
        }
