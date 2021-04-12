"""Web app for summarization of text."""
from flask import Flask
from flask_restful import Api
from resources.model import Model


app = Flask(__name__)
api = Api(app)

api.add_resource(Model, '/api/predict')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
