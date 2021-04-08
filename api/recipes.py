from flask_restx import Resource, Api, Namespace
from flask import request, jsonify

Recipes = Namespace(
    name="Recipes",
    description="APIs for recipes"
)


@Recipes.route('')
class RecipesInfo(Resource):
    def get(self):
        return{
            "test": "success"
        }
