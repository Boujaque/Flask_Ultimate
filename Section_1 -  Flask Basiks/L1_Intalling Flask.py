#pipenv install flask
# set FLASK_APP=app
# flask run




from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def index(name):
    # return '<h1>Hello World </h1>'
    return '<h1>Hello {}</h1>' .format(name)