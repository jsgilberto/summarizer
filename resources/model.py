from flask import Flask, jsonify, request
from flask_restful import Resource
from common.predictor import Summarizer


model = Summarizer(min_length=100, max_length=300)


class Model(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        text = json_data["text"]
        prediction = model.predict(text)
        return jsonify(prediction=prediction)
