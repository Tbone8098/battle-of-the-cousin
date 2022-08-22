from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import random


class Family(model_base.base_model):
    table = 'Families'

    def __init__(self, data):
        super().__init__(data)
        self.code = data['code']
        self.user_id = data['user_id']

    @classmethod
    def create(cls, **data):
        family_code = cls.gen_code()
        dict = {
            'code': family_code,
            'name': data['family_name'],
        }
        return super().create(**dict)

    @staticmethod
    def gen_code():
        options = [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['!', '@', '#', '$', '%', '^', '&', '*'],
        ]
        code = ""
        is_found = True
        while is_found:
            for indx in range(10):
                option = options[random.randint(0, len(options) - 1)]
                char = option[random.randint(0, len(option) - 1)]
                code += char
            if not Family.get_one(code = code):
                is_found = False
        return code



    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['column name']) < 1:
            errors['Family_column name'] = 'column nameis required'

        return errors
