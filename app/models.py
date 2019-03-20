# -*- coding: utf-8 -*-

from datetime import datetime
from app import db
from flask_login import UserMixin
from app import login

# классы, соответствующие таблицам в базе данных
class meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(64), index=True, unique=True)
    amount = db.Column(db.Float, index=True)
    price = db.Column(db.Float, index=True)
    categorie = db.Column(db.Integer, index=True)

    # функция для отображения блюд и отладки
    def __repr__(self):
        return '<Meal {}>'.format(self.meal)

class info_meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    callories = db.Column(db.Float, index=True)
    fats = db.Column(db.Float, index=True)
    proteins = db.Column(db.Float, index=True)
    carbohydrates = db.Column(db.Float, index=True)

class cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    new_id = db.Column(db.Integer, index=True)
    meal_id = db.Column(db.Integer, index=True)

    # функция для отображения блюд и отладки
    def __repr__(self):
        return '<Meal_id {}>'.format(self.meal_id)