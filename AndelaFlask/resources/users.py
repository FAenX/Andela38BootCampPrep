from flask import request
from flask_restful import Resource, abort
from models import db, User, UserSchema

user_schema = UserSchema()


class UserResource(Resource):
    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username)
        # user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return {'username': user.username}, 201
