# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import meals, info_meals, cart

class AddMealForm(FlaskForm):
    submit = SubmitField('Добавить в корзину')

class ClearCartForm(FlaskForm):
    submit = SubmitField('Очистить корзину')

class DeleteCartForm(FlaskForm):
    submit = SubmitField('Удалить блюдо')
