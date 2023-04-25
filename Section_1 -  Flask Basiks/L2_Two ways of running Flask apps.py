from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World from L2</h1>'

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()


    #metod 2 is using flask run  after definitiona of evironment variable:
    #export FLASK_APP=app.py (?)
    #to use debug mode:
    # export Flask_DEBYG=1
    #flask run