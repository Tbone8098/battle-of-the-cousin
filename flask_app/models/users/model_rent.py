from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app.models.users import model_user

from flask_app import DATABASE_SCHEMA
import re

class Rent(model_base.base_model):
    table = 'Rents'
    def __init__(self, data):
        super().__init__(data)
        self.email = data['email']
        self.user_id = data['user_id']

    @property
    def get_user(self):
        return model_user.User.get_one(id=self.user_id)

    @classmethod
    def create(cls, **data):
        print("&"*80)
        print(data)
        dict = {
            'user_id': data['user_id'],
            'email': data['email'],
        }
        return super().create(**dict)

    # Validator
    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['email']) < 1: 
            print("email is required")
            is_valid = False
            
        if len(data['user_id']) < 1: 
            print("user_id is required")
            is_valid = False
        
        return is_valid