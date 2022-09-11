from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Chores_has_days(model_base.base_model):
    table = 'chores_has_days'
    def __init__(self, data):
        super().__init__(data)