import uuid
from flask import request
from flask_restplus import Namespace, Resource, fields

api = Namespace('cos', description='Top level interaction with COs.')

@api.route('/')
class COs(Resource):
    def get(self):
        print(request.headers)
        print(request.headers.get('Y-HTTP-COOKIE'))
        print(request.cookies)
        return {'cos': 'all'}

@api.route('/<int:id>')
@api.doc(responses={404: 'CO not found'}, params={'co_id': 'The CO id'})
class CO(Resource):
    '''Show a CO that the provided identity has access to.'''
    @api.doc(description='co_id should be in...')
    def get(self, id):
        if id == 1:
            return {'co': 'single'}
        api.abort(404, message='CO {0} not found. Use different CO id.'.format(id), custum='')

    @api.response(204, 'CO successfully updated')
    def put(self, id):
        return None, 204
