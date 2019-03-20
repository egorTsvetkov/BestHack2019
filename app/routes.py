# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.models import meals, info_meals, cart
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import AddMealForm, ClearCartForm, DeleteCartForm
from importlib import reload


import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# функция для добавления блюда из меню в корзину
@app.route('/<int:id>/add_elem', methods=['POST'])
def add_elem(id):
    # выбираем из таблицы блюд блюдо с нужным индексом
    meal = meals.query.filter_by(id=id+1)

    # считаем число блюд, которые уже лежат в корзине, 
    # чтобы присвоить необходимый порядковый индекс (new_id)
    # потому что поле id нельзя изменить, т.к. оно автозаполняемое
    number = 1
    all_c = cart.query.all()
    for a in all_c:
        number += 1

    # добавляем элемент в козину в соответствии с видом таблицы
    # new_id - порядковый номер строки
    # meal_id - номер блюда в таблице meals
    elem = cart(new_id=number, meal_id=meal[0].id)
    db.session.add(elem)
    db.session.commit()
    # перенаправляем на index.html
    return redirect(url_for('index'))

# функция для отображения основной страницы (с меню)
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # выбираем из базы данных блюда по соответствующим номерам категорий
    food_salads = meals.query.filter_by(categorie=1)
    food_soup = meals.query.filter_by(categorie=2)
    food_second_meals = meals.query.filter_by(categorie=3)
    food_garniers = meals.query.filter_by(categorie=4)
    food_drinks = meals.query.filter_by(categorie=5)
    # создаем форму добавления элементов
    form_add = AddMealForm()
    # отображение index.html, куда передаются все необходимые элементы
    return render_template('index.html', title='COBROTIGETS', soups=food_soup, salads=food_salads, drinks=food_drinks, seconds=food_second_meals, garns=food_garniers, form_add=form_add)


# функция для удвления элемента из корзины
@app.route('/<int:id>/delete_elem', methods=['POST'])
def delete_elem(id):
    # выбираем элемент из корзины по индексу, который передается из html файла
    elem = cart.query.filter_by(new_id=id+1)
    # удаляем элемент
    for e in elem:
        db.session.delete(e)
        db.session.commit()

    # перенумеровываем все строки (new_id) в таблице cart
    all_c = cart.query.all()
    
    n = 1
    for e in all_c:
        e.new_id = n
        db.session.commit()
        n += 1
    # перенаправляем на cart.html
    return redirect(url_for('cart_func'))

# фуекция для отображения страницы корзины
@app.route('/cart', methods=['GET', 'POST'])
def cart_func():
    # получаем все элементы из корзины
    meals_cart = cart.query.all()
    meals_list = []

    # вводим переменные для количества блюд, общей суммы и количества
    total_amount = 0
    total_price = 0
    num_meals = 0

    # для каждого элемента создаем свою форму удаления элемента
    forms_delete = []
    for elem in meals_cart:
        m = meals.query.filter_by(id=elem.meal_id)
        total_price += float(m[0].price)
        total_amount += float(m[0].amount)
        num_meals += 1
        # заполнение списка блюд в корзине 
        meals_list.append(m[0])
        forms_delete.append(DeleteCartForm())

    # создаем форму для полного очищения корзины
    form_clear = ClearCartForm()
    # если нажать на кнопку, то таблица корзины очистится
    if form_clear.validate_on_submit():
        all_cart = cart.query.all()
        for elem in all_cart:
            db.session.delete(elem)
            db.session.commit()
        # перенаправление на cart.html
        return redirect(url_for('cart_func'))

    return render_template('cart.html', meals_list=meals_list, form_clear=form_clear, total_amount=total_amount, total_price=total_price, num_meals=num_meals, forms_delete=forms_delete)

