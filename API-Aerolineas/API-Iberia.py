from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/Iberia-sample-api', method=['GET'])
def hello():

    name = request.args.get('name')

    if name is None:

        text = "Hello!"

    else:

        text = "Hello ", name, "!"

    return jsonify({"message": text})
