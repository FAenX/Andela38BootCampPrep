from flask import Blueprint
from flask_restful import Api
from resources.andelan import AndelanResource
from resources.users import UserResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(AndelanResource, '/andelans')
api.add_resource(UserResource, '/users')