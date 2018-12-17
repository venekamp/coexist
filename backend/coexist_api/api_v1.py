from flask import Blueprint
from flask_restplus import Api

# api = Api(blueprint)

from coexist_api.apis.root import api as root
from coexist_api.apis.cos.cos import api as cos

blueprint = Blueprint('api v1', __name__, url_prefix='/api/v1')
api = Api(blueprint,
    title='coexist API',
    version='1.0',
    description='Group management with federative identities.',
)

api.add_namespace(root)
api.add_namespace(cos)
