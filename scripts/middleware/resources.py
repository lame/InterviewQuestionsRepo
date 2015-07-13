import requests
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class BasicInfo(Resource):

    def __init__(self):
        pass

    def get(self):
        return_dict = {}
        resp = requests.get('http://localhost:3000/api/vehicles')
        for key, value in resp.json().iteritems():
            return_dict[key] = {
                'make' = value['make']
                'model' = value['model']
            }
        return return_dict

class MoreInfo(Resource):

    def __init__(self):
        pass

    def get(self):
        in_data = request.get_json(force=True, silent=False)
        index_num = in_data['index_number']
        #  TODO: add error checking here
        resp = requests.get('http://localhost:3000/api/vehicles')
        return resp.json()[index_num]


api.add_resource(BasicInfo, '/api/basic_info')
api.add_resource(MoreInfo, '/api/more_info')

if __name__ == "__main__":
    app.run(debug=True)
