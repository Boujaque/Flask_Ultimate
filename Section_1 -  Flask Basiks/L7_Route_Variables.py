from flask import Flask, jsonify
#run code from start buton on PyCharm

app =Flask(__name__)


@app.route("/")
def index():
    return "<h1> Hello, World L7</h1>"
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
# @app.route('/home/<int:name>', methods=['POST', 'GET']) # using types this case integer
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the Home Page</h1>'.format(name)

@app.route("/products")
def products():
    return "<h2>Product List</h2>"
@app.route("/json")
def json():
    return jsonify({'key1': 'value', 'key2' : [1,2,3]})

if __name__ == '__main__':
    app.run()