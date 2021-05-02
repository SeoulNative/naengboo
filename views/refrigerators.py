from flask_restx import Resource, Api, Namespace
from database.models import Ingredients
from flask import jsonify
from daos.ingredients_dao import IngredientsDao
import ast
import json
Refrigerators = Namespace(
    name="Refrigerators",
    description="APIs for refrigerators"
)


@Refrigerators.route('')
class IngredientsTest(Resource):
    def get(self):
        ingredients_dao = IngredientsDao()
        ingredients_dao.add_ingredients({
            "category": "뾰루지",
            "name": "갈치",
            "icon_url": "http://hello.com"
        })
        ingredients = ingredients_dao.get_ingredient_list({
            "id": "608eb84e80c64480c436677b"
        })
        a = ingredients.to_json()
        return ast.literal_eval(a)