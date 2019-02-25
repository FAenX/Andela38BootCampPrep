from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# from passlib.apps import custom_app_context as pwd_context



ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    # def hash_password(self, password):
    #    self.password_hash = pwd_context.encrypt(password)

    #def verify_password(self, password):
    #    return pwd_context.verify(password, self.password_hash)


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password_hash = fields.String(required=True)
    creation_date = fields.DateTime()


class Andelan(db.Model):
    __tablename__ = 'andelans'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    language = db.Column(db.String(250), nullable=False)

    def __init__(self, first_name, language):
        self.first_name = first_name
        self.language = language


class AndelanSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    language = fields.String(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    creation_date = fields.DateTime()
