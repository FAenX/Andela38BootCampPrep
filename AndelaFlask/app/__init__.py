from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Andelans

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/andelans/', methods=['POST', 'GET'])
    def andelans():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            if name:
                andelan = Andelans(name=name)
                andelan.save()
                response = jsonify({
                    'id': andelan.id,
                    'name': andelan.name,
                    'date_created': andelan.date_created,
                    'date_modified': andelan.date_modified
                })
                response.status_code = 201
                return response
        else:
            # GET
            andelans = Andelans.get_all()
            results = []

            for andelan in andelans:
                obj = {
                    'id': andelan.id,
                    'name': andelan.name,
                    'date_created': andelan.date_created,
                    'date_modified': andelan.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/andelans/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def andelan_manipulation(id, **kwargs):
     # retrieve andelan using it's ID
        andelan = Andelans.query.filter_by(id=id).first()
        if not andelan:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            andelan.delete()
            return {
            "message": "andelan {} deleted successfully".format(andelan.id) 
         }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            andelan.name = name
            andelan.save()
            response = jsonify({
                'id': andelan.id,
                'name': andelan.name,
                'date_created': andelan.date_created,
                'date_modified': andelan.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': andelan.id,
                'name': andelan.name,
                'date_created': andelan.date_created,
                'date_modified': andelan.date_modified
            })
            response.status_code = 200
            return response


    return app