from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# from passlib.apps import custom_app_context as pwd_context

ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):

    __table__ = 'users'
    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    creation_date=db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # def hash_password(self, password):
    #    self.password_hash = pwd_context.encrypt(password)

    # def verify_password(self, password):
    #    return pwd_context.verify(password, self.password_hash)

class UserSchema(ma.Schema):
    id = fields.Integer()
    username = fields.String(required=True)
    password_hash = fields.String(required=True)
    creation_date = fields.DateTime()


class BlogPost(db.Model):

    __table__='blog post'
    id = db.Column(db.Interger, primary_key=True)
    post = db.Column(db.String())
    creation_date=db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False
    )

    def __init__(self, post):
        self.post = post


class BlogPostSchema(ma.Schema):
    id = fields.Interger()
    post = fields.String(required=True)
    creation_date = db.DateTime()


class Comment(db.Model):
    pass