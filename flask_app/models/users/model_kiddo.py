from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_chore
from flask_app import DATABASE_SCHEMA
import re

class Kiddo(model_base.base_model):
    table = 'Kiddos'
    def __init__(self, data):
        super().__init__(data)
        self.battlename = data['battlename']
        self.user_id = data['user_id']

    @classmethod
    def get_one_by_user_id_with_chores(cls, **data):
        query = "SELECT * FROM kiddos LEFT JOIN chores ON kiddos.id = chores.kiddo_id WHERE kiddos.user_id = %(user_id)s"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        if not results:
            return False
        kiddo = cls(results[0])
        if not results[0]['chores.id']:
            return kiddo
        all_chores = []
        for dict in results:
            chore_dict = {
                **dict,
                'id': dict['chores.id'],
                'created_at': dict['chores.created_at'],
                'updated_at': dict['chores.updated_at'],
            }
            all_chores.append( model_chore.Chore(chore_dict) )
        kiddo.chores = all_chores
        return kiddo





    # Validator
    @staticmethod
    def validation(data):
        is_valid = True

        if len(data['battlename']) < 1: 
            is_valid = False
            print('battlename is required')
        
        return is_valid