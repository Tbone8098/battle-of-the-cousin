from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_base
from flask_app.models.users import model_user
from flask_app import DATABASE_SCHEMA
from flask import redirect
import random


class Family(model_base.base_model):
    table = 'Families'

    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.code = data['code']

    @classmethod
    def get_one_with_members(cls, **data):
        query = "SELECT * FROM families JOIN users ON users.family_id = families.id WHERE families.id = %(id)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if not results:
            return []
        family = cls(results[0])
        members = [] 
        for dict in results:
            user_data = {
                **dict,
                'id': dict['users.id'],
                'created_at': dict['users.created_at'],
                'updated_at': dict['users.updated_at'],
            }
            members.append( model_user.User(user_data))
        family.members = members
        return family


    @classmethod
    def create(cls, **data):
        family_code = cls.gen_family_code()
        # validate
        data = {
            **data,
            'family_code': family_code
        }
        if not cls.validate(**data, ):
            print("family validation err")
            return False
        
        data = {
            'code': family_code,
            'name': data['family_name'],
        }
        return super().create(**data)
        

    @classmethod
    def get_one_by_code(cls, **data):
        query = "SELECT * FROM families WHERE code = %(code)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @staticmethod
    def gen_family_code() -> str:
        """Generate a family code for a newly created family

        Returns:
            str: family code
        """
        options = [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['!', '@', '#', '$', '%', '^', '&', '*', ],
        ]
        code = ''
        already_exists = True
        while already_exists:
            for idx in range(10):
                option = options[random.randint(0, len(options) - 1)]
                char = option[random.randint(0,len(option) - 1)]
                code += char
            if not Family.get_one_by_code(code=code):
                already_exists = False
        return code

    @staticmethod
    def validate(**data:dict) -> bool:
        """will validate a dictionary to make sure it has all the appropriate values for the class
        """
        is_valid = True

        if len(data['family_name']) < 1:
            is_valid = False

        if len(data['family_code']) < 1:
            is_valid = False

        return is_valid


