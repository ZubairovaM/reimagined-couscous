from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route('/')
def begin():
    return f"""
ссылка на <a href="/base">базовую</a> страницу<br>
ссылка на <a href="/start">стартовую</a> страницу<br>
ссылка на <a href={url_for("index")}>index</a> страницу<br>
ссылка на <a href={url_for("form")}>страницу с формой</a>"""


@app.route('/index')
def index():
    username = 'Stolyarov'
    return render_template('index.html', username=username)


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/base')
def base():
    return render_template(f'base.html')


@app.route('/start')
def start():
    return render_template(f'start.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for item in request.form:
            print(item , request.form[item])
    return render_template('form.html')


if __name__ == '__main__':
    app.run(port=1060, debug=True)
