from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello world"

@app.route('/produtos', methods="['GET']")
def products():
    return "Carros"

app.run(host='127.0.0.1', port=3000)