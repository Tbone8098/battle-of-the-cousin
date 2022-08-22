from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA, bcrypt
import re


class User(model_base.base_model):
    table = 'Users'

    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.level = data['level']
        self.pw = data['pw']
        self.family_id = data['family_id']

    @classmethod
    def create(cls, **data):
        dict = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'level': data['level'],
            'pw': data['pw'],
            'confirm_pw': data['confirm_pw'],
            'family_id': data['family_id'],
        }
        if not cls.validation(dict):
            return False
        dict['pw'] = bcrypt.generate_password_hash(data['pw'])
        del dict['confirm_pw']
        return super().create(**dict)

    # Validator

    @staticmethod
    def validation(data):
        is_valid = True
        print(data)

        if len(data['first_name']) < 1:
            print("first_name is required")
            is_valid = False

        if len(data['last_name']) < 1:
            print("last_name is required")
            is_valid = False

        if len(data['pw']) < 1:
            print("pw is required")
            is_valid = False

        if 'level' not in data:
            print("level is required")
            is_valid = False

        if 'family_id' not in data:
            print("family_id is required")
            is_valid = False

        if data['confirm_pw'] != data['pw']:
            print("passwords do not match")
            is_valid = False

        return is_valid
