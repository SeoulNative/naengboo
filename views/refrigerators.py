from flask_restx import Resource, Api, Namespace
from database.models import Ingredients
from flask import jsonify


Refrigerators = Namespace(
    name="Refrigerators",
    description="APIs for refrigerators"
)


@Refrigerators.route('')
class IngredientsTest(Resource):
    def get(self):
        ingredients = Ingredients.objects()
        return jsonify(ingredients.to_json())
