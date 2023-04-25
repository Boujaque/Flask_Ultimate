from flask import Flask, jsonify, request
#run code from start buton on PyCharm

app =Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello, World L8</h1>"
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
# @app.route('/home/<int:name>', methods=['POST', 'GET']) # using types this case integer
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the Home Page</h1>'.format(name)

@app.route("/json")
def json():
    return jsonify({'key1': 'value', 'key2' : [1,2,3]})

@app.route("/query")
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return "<h2>Hi {}, You are from {}</h2>".format(name, location)
# http://127.0.0.1:5000/query?name=Sara&location=Florida
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['input_data'] # assuming 'input_data' is the name of the input field in the HTML form
    # do something with the data
    return f'Thanks for submitting {data}!'

if __name__ == '__main__':
    app.run()