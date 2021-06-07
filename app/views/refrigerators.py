from flask_restx import Namespace, Resource
from flask import request, jsonify
from bson.json_util import dumps
from app import db


Refrigerators = Namespace(
    name="Refrigerators",
    description="APIs for refrigerators"
)


# TODO(livlikwav): fix this with dao & model
# test db connection
@Refrigerators.route('/ingredients')
class Ingredients(Resource):
    def post(self):
        # parse post request body
        req_json = request.json

        # post one document
        test = db['test']
        test.insert_one(req_json)

        # query the post result
        result = test.find()
        resp = dumps(result)

        return jsonify(resp)
