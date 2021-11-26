from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/meat/", methods=['GET'])
def get():

    search_term = request.args.get('search_term')

    with open("/data.json", "r") as datafile:
        recipes = json.load(datafile)

    response = [ recipe for recipe in recipes['recipes'] if search_term in recipe['recipe_title'] ]
    return jsonify({"recipes":response})

@app.route("/meat/", methods=['PUT'])
def put():

    request_data = json.loads(request.data)

    with open("/data.json", "r") as datafile:
        recipes = json.load(datafile)

    recipes['recipes'].append(request_data)

    with open("/data.json", "w") as datafile:
        datafile.write(json.dumps(recipes))

    return jsonify(request_data)

@app.route("/meat/", methods=['POST'])
def post():

    request_data = json.loads(request.data)

    with open("/data.json", "r") as datafile:
        recipes = json.load(datafile)

    found = False

    for recipe in recipes['recipes']:
        if recipe["recipe_title"] == request_data['recipe_title']:
            recipe["recipe_title"] = request_data['recipe_title']
            recipe["recipe_text"] = request_data['recipe_text']
            found = True

    if found:
        with open("/data.json", "w") as datafile:
            datafile.write(json.dumps(recipes))

    return jsonify(request_data) if found else jsonify("Could not find recipe")

@app.route("/meat/", methods=['DELETE'])
def delete():

    request_data = json.loads(request.data)

    with open("/data.json", "r") as datafile:
        recipes = json.load(datafile)

    found = False

    for recipe in recipes['recipes']:
        if recipe["recipe_title"] == request_data['recipe_title']:
            recipes['recipes'].remove(recipe)
            found = True

    if found:
        with open("/data.json", "w") as datafile:
            datafile.write(json.dumps(recipes))

    return jsonify(request_data) if found else jsonify("Could not find recipe")

