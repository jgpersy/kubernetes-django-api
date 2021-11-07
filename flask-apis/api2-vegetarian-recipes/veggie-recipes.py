from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/vegetarian/")
def respond():
    response = {"message":"Hello from vegetarian recipes api!"}
    return jsonify(response)