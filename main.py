#!/usr/bin/python
# coding: utf-8
from flask import Flask, request

from perceptron import predictor

app = Flask(__name__)


@app.route('/er', methods=['GET'])
def entry_point():
    try:
        n_iterations = request.args.get("n_iterations")
        random_state = request.args.get("random_state")
        learning_rate = request.args.get("learning_rate")
        n_iterations = int(n_iterations) if n_iterations else 100
        random_state = int(random_state) if random_state else 1
        learning_rate = float(learning_rate) if random_state else 0.01
        return {'solution': predictor(n_iterations, random_state, learning_rate)}
    except Exception:
        return ({'error': 'Error obtaining data'})


if __name__ == '__main__':
    app.run(debug=True)
