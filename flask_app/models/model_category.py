from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Category(model_base.base_model):
    table = 'Categories'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.family_id = data['family_id']