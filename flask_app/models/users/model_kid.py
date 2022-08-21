from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app.models.users import model_user
from flask_app import DATABASE_SCHEMA, bcrypt
import re


class Kid(model_base.base_model):
    table = 'Kids'

    def __init__(self, data):
        super().__init__(data)
        self.username = data['username']
        self.pin = data['pin']
        self.user_id = data['user_id']

    @property
    def user_info(self):
        return model_user.User.get_one(id=self.user_id)

    @classmethod
    def create(cls, **data):
        # validate 
        if not cls.validate(**data):
            print("parent validation err")
            return False

        hash_pin = bcrypt.generate_password_hash(data['pin'])
        data = {
            'username': data['username'],
            'user_id': data['user_id'],
            'pin': hash_pin
        }
        return super().create(**data)

    @staticmethod
    def validate(**data):
        is_valid = True

        if len(data['username']) < 1:
            print("username is required")
            is_valid = False
        if len(data['pin']) < 1:
            print("pin is required")
            is_valid = False

        return is_valid