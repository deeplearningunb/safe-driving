from flask_restful import Resource, reqparse

class Prediction(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        data = Prediction.parser.parse_args()

        return {"message": "200"}

