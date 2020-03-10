from flaskapp.ext.database import db
from flaskapp import known_exceptions
from sqlalchemy_serializer import SerializerMixin


class AbstractModel(db.Model, SerializerMixin):
    __abstract__ = True

    @classmethod
    def get(cls, id):
        return cls.query.get(id)

    @classmethod
    def filter_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def filter_by_expression(cls, expression):
        return cls.query.filter(expression)

    @classmethod
    def one_or_none(cls, **kwargs):
        return cls.filter(**kwargs).one_or_none()

    @classmethod
    def list_all(cls):
        return cls.query.all()

    @classmethod
    def list_all_paged(cls, start_at, size):
        return cls.query.order_by("id").offset(start_at).limit(size).all()

    @classmethod
    def order_by(cls, **kwargs):
        return cls.query.order_by(**kwargs)

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def create_from_dict(cls, json_data):
        try:
            instance = cls()
            instance.set_values(json_data)
            instance.save_db()
            return instance
        except Exception as ex:
            pass
            raise known_exceptions.RepositoryError(str(ex))

    @classmethod
    def execute_statement(cls, statement):
        try:
            db.session.execute(statement)
            db.session.commit()
        except Exception as ex:
            raise known_exceptions.RepositoryError(str(ex))

    def update_instance_from_dict(self, json_data):
        try:
            self.set_values(json_data)
            self.save_db()
            return self
        except Exception as ex:
            raise known_exceptions.RepositoryError(str(ex))

    def delete_instance(self):
        try:
            id = self.id
            self.delete_db()
            return id
        except Exception as ex:
            raise known_exceptions.RepositoryError(str(ex))

    def save_db(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        else:
            db.session.flush()

    def delete_db(self):
        db.session.delete(self)
        db.session.commit()

    def set_values(self, json_data):
        for key, value in json_data.items():
            setattr(self, key, json_data.get(key, getattr(self, key)))
