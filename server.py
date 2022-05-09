from flask import Flask, render_template, url_for, request, flash, abort, session, redirect
from time import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'agdfgdfsgjhsj;dfghs;ed'

users = [
    {'username': 'alex', 'password':'12345'},
    {'username': 'Kate', 'password':'12345'},
    {'username': 'Helen', 'password':'12345'},
    {'username': 'dima', 'password':'12345'}
]

@app.route('/')
def begin():
    return f"""
                Ссылка на <a href = {url_for('base')}>базовую</a>страницу<br>
                Ссылка на <a href = {url_for('start')}>стартовую</a>страницу<br>
                Ссылка на <a href = {url_for('index')}>index</a>страницу<br>
                Ссылка на <a href={url_for("form")}>страницу с формой</a><br>
                Ссылка на <a href={url_for("login")}>страницу авторизации</a><br>
            """

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')

@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')

@app.route('/base')
def base():
    return render_template('index-base.html')

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for item in request.form:
            print(item, request.form[item])
    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if request.form['username'] == user['username']:
                if request.form['password'] == user['password']:
                    session['logged_in'] = True
                    return redirect(f"/profile/{user['username']}")
                else:
                    break
        flash('Неправильный логин и/или пароль', category='error')
    return render_template('login.html')

@app.route('/profile/<username>')
def profile(username):
    for user in users:
        if user['username'] == username:
            if 'logged_in' in session:
                if session['logged_in'] == True:
                    return render_template('profile.html', username=username)
            else:
                abort(403)
            flash('Вам туда нельзя', category='error')
            return redirect(url_for('login'))
    abort(404)

if __name__ == '__main__':
    app.run(port=1060, debug=True)