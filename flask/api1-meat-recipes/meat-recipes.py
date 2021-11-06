from flask import Flask

app = Flask(__name__)

@app.route("/meat/")
def hello_world():
    return "<p>Meat-recipes-api</p>"