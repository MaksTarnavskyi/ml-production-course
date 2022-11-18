from flask import Flask, jsonify
from flask_restplus import Api, Resource, fields
from model.predictor import Predictor


app = Flask(__name__)
api = Api(app, version='1.0', title='Flask API', description='A simple Flask API',)
predictor = Predictor.default_from_model_registry()

ns = api.namespace('nlp-model', description='model operation')
model_response = api.model('ModelResponse', {
    'probs': fields.List(fields.Float, required=True, description='probs')
})

@ns.route('/<str: text>')
@ns.param('text', 'text to use for prediction')
class ApiPredictor(Resource):
    @ns.doc('trigger prediction of model')
    @ns.marshal_with(model_response)
    def predict(self, text: str):
        result = predictor.predict([text])
        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
