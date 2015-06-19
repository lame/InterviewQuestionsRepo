from flask.ext.restful import Resource


class VSMResource(Resource):

    def get(self):
        return 'hello world'
