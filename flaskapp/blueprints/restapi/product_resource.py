from flask import abort, jsonify
from flask_restplus import Resource, fields
from flaskapp.blueprints.restapi.singleton_api import SingletonApi
from flaskapp.models import Product

api = SingletonApi.get_instance()

model = api.model('Product', {
    'id': fields.Integer(),
    'name': fields.String(),
    'price': fields.Integer,
    'description': fields.String()
})


class ProductResource(Resource):

    def get(self):
        products = Product.query.all() or abort(204)
        return jsonify(
            {"products": [product.to_dict() for product in products]}
        )


class ProductItemResource(Resource):

    @api.expect(model)
    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first() or abort(404)
        return jsonify(product.to_dict())
