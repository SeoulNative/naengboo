from flask import Flask
from flask_restx import Api, Resource
from views.recipes import Recipes
from views.refrigerators import Refrigerators
from views.user import User

app = Flask(__name__)
api = Api(app)

api.add_namespace(Recipes, '/recipes')
api.add_namespace(Refrigerators, '/refrigerators')
api.add_namespace(User, '/user')


@api.route('/test')
class Test(Resource):
    def get(self):
        return {"message": "test success"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
