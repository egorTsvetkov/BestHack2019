# BESTHack-Cobrotigers
Web-app for Cobrotigers

Запуск виртуального окружения
cd newapp
virtualenv venv
source venv/bin/activate
pip install flask
export FLASK_APP=newapp.py

Для загружения необходиых зависимостей
pip install flask-wtf flask-sqlalchemy flask-migrate flask-login

Для инициализации базы данных можно использовать
sqlite3 app.db
.read db_init.sql
.quit

Для запуска приложения использовать в виртуальной среде 
flask run 

Архитектура приложения имеет следующий вид:
1) Есть база данных, которая заполняется с помощью файла db_init.sql
2) В файле __init__.py указаны необходимые зависимости для использования фреймворка Flask для языка python, а также для использования SQLAlchemy для управления базами данных
3) В файле models.py находятся описания классов, соответсвующие таблицам в базе данных app.db
4) В файле routes.py описана основная архитектура приложени
    /index - страница с меню и возможностью добавить элементы, используя /<int:id>/add_elem
    /cart - страница с корзиной и возможностью удалить оттуда элементы, используя /<int:id>/delete_elem
5) В файле errors.py - перенаправление на собственный шаблон ошибок (404 и 500)
6) В файле forms.py - классы, наследующие WTForms, для добавления или удаления элементов
7) В папке templates - шаблоны html страниц

В html-страницах есть форму, которые имеют action="{{ url_for('add_elem', id=vars.ind) }}" (например), это значит, что мы вызовем функцию add_elem c параметром id=vars.ind, который уникален для каждой отображаемой строчки (Это реализовано с помощью переменных Jinja2)