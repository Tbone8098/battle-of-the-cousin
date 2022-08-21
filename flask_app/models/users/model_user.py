from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app.models.users import model_family
from flask_app import DATABASE_SCHEMA
from flask import redirect
import re


class User(model_base.base_model):
    table = 'Users'

    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.family_id = data['family_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.is_parent = data['is_parent']
        self.fullname = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    @property
    def family(self):
        return model_family.Family.get_one(id=self.family_id)

    @property
    def family_with_members(self):
        return model_family.Family.get_one_with_members(id=self.family_id)

    @classmethod
    def create(cls, **data):
        if not cls.validate(**data):
            return False

        data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'family_id': data['family_id'],
            'is_parent': data['is_parent'],
        }
        return super().create(**data)

    @staticmethod
    def validate(**data):
        is_valid = True
        
        print(data)

        if len(data['first_name']) < 1:
            print(f"first_name is required")
            is_valid = False
        if len(data['last_name']) < 1:
            print(f"last_name is required")
            is_valid = False
        if 'family_id' not in data:
            print(f"family_id is required")
            is_valid = False
        

        return is_valid
