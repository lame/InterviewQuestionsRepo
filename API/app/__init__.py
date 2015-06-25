from flask import Flask
from flask.ext.cors import CORS
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')

cors = CORS(app)
api = Api(app)
