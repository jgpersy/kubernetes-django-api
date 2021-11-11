from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/meat/")
def respond():
    response = {"message":"Hello from meat recipes api v2!"}
    return jsonify(response)