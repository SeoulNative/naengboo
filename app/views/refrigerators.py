from flask_restx import Namespace, Resource
from flask import jsonify
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
        # post one document
        test = db['test']
        test.insert_one({'username' : 'db-test','msg' : 'wow it works'})
        
        # query the post result
        result = test.find()
        for doc in result:
            resp = dumps(doc)
        return jsonify(resp)
