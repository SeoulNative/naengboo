from flask_restx import Resource, Api, Namespace
from database.models import Ingredients
from flask import jsonify
from database.daos.ingredients_dao import IngredientsDao
Refrigerators = Namespace(
    name="Refrigerators",
    description="APIs for refrigerators"
)


@Refrigerators.route('')
class IngredientsTest(Resource):
    def get(self):
        ingredients_dao = IngredientsDao()
        ingredients_dao.add_ingredients({
            "category": "해산물",
            "name": "갈치",
            "icon_url": "http://hello.com"
        })
        ingredients = ingredients_dao.model.objects()
        return jsonify(ingredients.to_json())
