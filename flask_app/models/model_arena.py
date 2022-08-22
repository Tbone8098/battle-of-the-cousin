from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Arena(model_base.base_model):
    table = 'Arenas'
    def __init__(self, data):
        super().__init__(data)


    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['column name']) < 1: 
            errors['Arena_column name'] = 'column nameis required'
        
        return errors