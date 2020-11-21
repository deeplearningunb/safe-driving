from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.prediction import Prediction

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
CORS(app)

api.add_resource(Prediction, '/v1/safe-driving/predictions')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)