"""Resources related to the machine learning model for summarization."""
from flask import jsonify, request
from flask_restful import Resource
from common.predictor import Summarizer


model = Summarizer(min_length=100, max_length=300)


class Model(Resource):
    """Resource used to interact with the model."""

    def post(self):
        """Post method for getting predictions given some text.

        Returns:
            Any: the json response
        """
        json_data = request.get_json(force=True)
        text = json_data["text"]
        prediction = model.predict(text)
        return jsonify(prediction=prediction)
