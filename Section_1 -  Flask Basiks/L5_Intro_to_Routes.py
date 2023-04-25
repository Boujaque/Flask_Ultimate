from flask import Flask, jsonify
#run code from start buton on PyCharm

app =Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello, World L5</h1>"
@app.route("/home")
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