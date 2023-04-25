from flask import Flask, jsonify
#run code from start buton on PyCharm

app =Flask(__name__)
# @app.route allow only method  GET if we went to use other
# methods we need to specify them.

@app.route("/")
def index():
    return "<h1> Hello, World L5</h1>"
# @app.route("/home", methods=['GET'])
# @app.route("/home", methods=['POST']) #return method not allowed
@app.route('/home', methods=['POST', 'GET']) #return method not allowed
def home():
    return "<h1> Home Page</h1>"


@app.route("/products")
def products():
    return "<h2>Product List</h2>"
@app.route("/json")
def json():
    return jsonify({'key1': 'value', 'key2' : [1,2,3]})

if __name__ == '__main__':
    app.run()