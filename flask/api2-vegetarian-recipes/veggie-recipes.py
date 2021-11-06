from flask import Flask

app = Flask(__name__)

@app.route("/vegetarian/")
def hello_world():
    return "<p>Veggie-recipes-api</p>"