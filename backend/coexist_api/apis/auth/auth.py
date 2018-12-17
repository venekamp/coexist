import uuid
from flask import request, redirect
from flask_restplus import Namespace, Resource, fields

api = Namespace('/', description='Authenrication functions.')

@api.route('/login')
class COs(Resource):
    '''Let users login and retieve some of their provided claims.'''
    @api.doc(description='Let the user log in and retrieve user info.')
    def get(self):
        print(request.headers)
        print(request.cookies)
        return redirect('http://nos.nl/', code=302)

@api.route('/logout')
@api.doc(responses={404: 'CO not found'})
class CO(Resource):
    def get(self):
        return {'logout': 'user'}
