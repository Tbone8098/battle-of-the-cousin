from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app.models.users import model_user
from flask_app import DATABASE_SCHEMA, bcrypt
from flask import redirect
import re


class Parent(model_base.base_model):
    table = 'Parents'

    def __init__(self, data):
        super().__init__(data)
        self.email = data['email']
        self.user_id = data['user_id']
        self.pw = data['pw']

    @property
    def user_info(self):
        return model_user.User.get_one(id=self.user_id)

    @classmethod
    def create(cls, **data):
        # validate 
        if not cls.validate(**data):
            print("parent validation err")
            return redirect('/')

        hash_pw = bcrypt.generate_password_hash(data['pw'])
        data = {
            'email': data['email'],
            'user_id': data['user_id'],
            'pw': hash_pw
        }
        return super().create(**data)

    
    @staticmethod
    def validate(**data):
        is_valid = True

        if len(data['email']) < 1:
            print(f"email is required")
            is_valid = False
        if len(data['pw']) < 1:
            print(f"pw is required")
            is_valid = False
        if data['pw'] != data['confirm_pw']:
            print(f"pw and confirm pw do not match")
            is_valid = False

        return is_valid
