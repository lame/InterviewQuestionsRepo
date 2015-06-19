from config import api
from resources.vsm_resource import VSMResource

api.add_resource(VSMResource, '/api/vsm')
