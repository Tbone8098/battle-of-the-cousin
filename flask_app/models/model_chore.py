from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_category, model_day
from flask_app import DATABASE_SCHEMA

class Chore(model_base.base_model):
    table = 'chores'
    def __init__(self, data):
        super().__init__(data)
        self.title = data['title']
        self.description = data['description']
        self.difficulty_id = data['difficulty_id']
        self.category_id = data['category_id']

    @property
    def get_category(self):
        return model_category.Category.get_one(id=self.category_id)

    @property
    def get_days(self):
        query = f"SELECT * FROM days JOIN chores_has_days ON chores_has_days.day_id = days.id WHERE chores_has_days.chore_id = {self.id}"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if not results:
            return []
        all_days = []
        for dict in results:
            all_days.append( model_day.Day(dict) )
        return all_days