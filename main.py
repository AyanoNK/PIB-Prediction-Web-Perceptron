#!/usr/bin/python
# coding: utf-8
from flask import Flask, request
from flask_cors import CORS

from perceptron import predictor

app = Flask(__name__)
CORS(app)


@app.route('/prediction', methods=['GET'])
def entry_point():
    try:
        n_iterations = request.args.get("n_iterations")
        random_state = request.args.get("random_state")
        learning_rate = request.args.get("learning_rate")
        print(n_iterations, random_state, learning_rate)
        n_iterations = int(n_iterations) if n_iterations else 100
        random_state = int(random_state) if random_state else 1
        learning_rate = float(learning_rate) if random_state else 0.01
        return {'msg': predictor(n_iterations, random_state, learning_rate)}
    except Exception:
        return {'msg': 'Error obteniendo data'}


if __name__ == '__main__':
    app.run(debug=True)
