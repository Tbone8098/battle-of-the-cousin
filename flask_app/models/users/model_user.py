from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import model_base
from flask_app.models.users import model_user, model_family, model_rent, model_kiddo
from flask_app import DATABASE_SCHEMA, bcrypt
import re


class User(model_base.base_model):
    table = 'Users'

    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.level = data['level']
        self.family_id = data['family_id']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @property
    def get_user(self):
        return self.get_one(id = self.id)

    @property
    def family(self):
        return model_family.Family.get_one(id = self.family_id)

    @property
    def get_pw(self):
        query = f"SELECT pw FROM users WHERE id = {self.id}"
        result = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if not result:
            return False
        return result[0]['pw']

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

    @classmethod
    def create_user(cls, **data:dict):
        if 'is_kiddo' in data:
            return cls.build_kiddo(**data)
        return cls.build_rent(**data)

    @classmethod
    def build_kiddo(cls, **data:dict):
        family_id = cls.get_one(id=session['uuid']).family_id
        if not 'family_id':
            return False

        user_data = {
            **data,
            'level': 0,
            'family_id': family_id
        }
        user_id = cls.create(**user_data)
        if not user_id:
            return False
        
        kiddo_data = {
            'user_id': user_id,
            'battlename': data['battlename']
        }
        kiddo_id = model_kiddo.Kiddo.create(**kiddo_data)
        if not 'kiddo_id':
            return False
            
        return True

    @classmethod
    def build_rent(cls, **data:dict):
        if 'join_family' not in data:
            data['family_id'] = model_family.Family.create(**data)
        else:
            data['family_id'] = model_family.Family.get_one(code = data['family_code']).id
        session['family_id'] = data['family_id']
        if not data['family_id']: # check to make sure family was created
            return False

        user_data = {
                **data,
                'family_id': data['family_id'],
                'level': 1,
            }
        data['user_id'] = model_user.User.create(**user_data)
        if not data['user_id']: # check to make sure user was created
            return False

        data['rent_id'] = model_rent.Rent.create(**data)
        if not data['rent_id']: # check to make sure rent was created
            return False
            
        session['uuid'] = data['user_id']
        return True

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
