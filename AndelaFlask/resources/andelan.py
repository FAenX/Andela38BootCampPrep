from flask import request
from flask_restful import Resource
from models import db, Andelan, AndelanSchema, User
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


andelans_schema = AndelanSchema(many=True)
andelan_schema = AndelanSchema()


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.password_hash == password:
        return False
    return True


class AndelanResource(Resource):
    @auth.login_required
    def get(self):
        andelans = Andelan.query.all()
        andelans = andelans_schema.dump(andelans).data
        return {'status': 'success', 'data': andelans}, 200

    @auth.login_required
    def post(self):
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        language = request.json.get('language')
        andelan = Andelan(first_name=first_name,
                          last_name=last_name, language=language)
        db.session.add(andelan)
        db.session.commit()
        return {'status': 'success', 'andelan': andelan.__repr__()}

    @auth.login_required
    def put(self):
        data = request.get_json(force=True)
        if not data:
               return {'message': 'No input data provided'}, 400
        data, errors = andelan_schema.load(data)
        if errors:
            return errors, 422
        andelan = Andelan.query.filter_by(id=data['id']).first()
        if not andelan:
            return {'message': 'Andelan does not exist'}, 400
        andelan.first_name = data['first_name']
        andelan.last_name = data['last_name']
        andelan.language = data['language']
        db.session.commit()

        result = andelan_schema.dump(andelan).data
        return { "status": 'success', 'data': result }, 204

    @auth.login_required
    def delete(self):
        pass

