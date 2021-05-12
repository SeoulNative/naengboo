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


@Refrigerators.route('/ingredients')
class Ingredients(Resource):
    def get(self):
        ingredients_dao = IngredientsDao()
        ingredients_dao.add_ingredients({
            "category": "생선",
            "name": "갈치",
            "icon_url": "http://hello.com"
        })
        ingredients_dao.add_ingredients({
            "category": "양념",
            "name": "지코바소스",
            "icon_url": "http://hello.com"
        })
        ingredients = ingredients_dao.get_ingredient_list({
        })
        a = ingredients.to_json()
        return ast.literal_eval(a)