from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Kiddo(model_base.base_model):
    table = 'Kiddos'
    def __init__(self, data):
        super().__init__(data)


    # Validator
    @staticmethod
    def validation(data):
        errors = {}

        if len(data['column name']) < 1: 
            errors['Kiddo_column name'] = 'column nameis required'
        
        return errors