from flask_restx import Namespace, Resource
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
        test = db['test']
        test.insert_one({'username' : 'db-test','msg' : 'wow it works'})

        return {
            "result" : "success"
        }
