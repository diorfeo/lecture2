from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/sebas")
def sebas():
    return "Hola, diorfeo!"
