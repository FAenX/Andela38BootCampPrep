from flask import request
from flask_restful import Resource
from models import db, Andelan, AndelanSchema
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


andelans_schema = AndelanSchema(many=True)
andelan_schema = AndelanSchema()


class AndelanResource(Resource):
    @auth.login_required
    def get(self):
        andelans = Andelan.query.all()
        andelans = andelans_schema.dump(andelans).data
        return {'status': 'success', 'data': andelans}, 200