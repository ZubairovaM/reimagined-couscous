from flask import Flask, render_template
from time import *


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        for


if __name__ == '__main__':
    app.run(debug=True)


