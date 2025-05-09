from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/order')
def order_form():
    return render_template('order.html')

@main.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    surname = request.form['surname']
    city = request.form['city']
    post_office = request.form['post_office']
    phone = request.form['phone']

    # Сохранение данных в файл (например, блокнот)
    with open("orders.txt", "a") as file:
        file.write(f"Имя: {name} {surname}\nГород: {city}\nОтделение: {post_office}\nНомер: {phone}\nДата: {datetime.now()}\n\n")

    # Перенаправление на страницу с подтверждением
    return render_template('confirmation.html')

@main.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
