from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/test')
class Test(Resource):
    def get(self):
        return {"message" : "test success"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)