import click
from flaskapp.ext.database import db
from flaskapp.ext.auth import create_user
from flaskapp.models import Product


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def populate_db():
    data = [
        Product(
            id=1, name="NVIDIA GeForce GTX 1660 ", price="1000", description="Super video board"
        ),
        Product(id=2, name="Headset Gamer Razer", price="300", description="Headset Gamer Razer Electra V2 7.1 Virtual - USB"),
        Product(id=3, name="Xiaomi Mi 9T", price="2500", description="Smartphone Xiaomi Mi 9T, 128GB, 48MP, Tela 6.39"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Product.query.all()


def init_app(app):
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)
