from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


# Создаём функцию для обработки главных страниц
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Misha'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was so cool'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)  # То что возвращаем по итогу


# Создаём функцию для авторизации пользователей
@app.route('/login', methods=['GET', 'POST'])  # methods принимает запросы 'GET' и 'POST'
def login():
    form = LoginForm()
    if form.validate_on_submit():  # Пропускается при 'GET',так как form.validate_on_submit()=False
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))  # Вывод сообщения пользователю
        return redirect(url_for('login'))  # Перенаправление на страницу '/index'
    return render_template('login.html', title='Sign in', form=form)


@app.route('/about')
def about():
    return render_template('about.html')
