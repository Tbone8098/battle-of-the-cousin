from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Difficulty(model_base.base_model):
    table = 'difficulties'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.points_low = data['points_low']
        self.points_heigh = data['points_high']
