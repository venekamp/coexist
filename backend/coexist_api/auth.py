from flask import Blueprint
from flask_restplus import Api

from coexist_api.apis.auth.auth import api as auth

blueprint = Blueprint('Authentication API', __name__, url_prefix='/auth')
api = Api(blueprint,
    title='coexist authentication API',
    version='v1',
    description='Let users login and retieve some of their provided claims.',
)

api.add_namespace(auth)
