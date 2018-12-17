import uuid
from flask import Flask, make_response, request
from flask_restplus import Namespace, Resource, fields

api = Namespace('/', description='Support functions.')

@api.route('/csrftoken')
class csrftoken(Resource):
    cookie_name = "csrftoken"
    cookie_max_age = 60*60*24

    @api.doc(responses={
        200: "Return a CSRF token and set an http only cookie '{0}' with the same value. The cookie will be valid for {1:.2g} day(s).".format(cookie_name, cookie_max_age/(60*60*24))
        })
    def get(self):

        if not request.cookies.get(self.cookie_name):
            token = str(uuid.uuid4())
            resp = make_response(token)
            resp.set_cookie(self.cookie_name,
                    value=token,
                    httponly=True,
                    max_age=self.cookie_max_age,
                    samesite="strict"
                    )
        else:
            resp = make_response(request.cookies.get(self.cookie_name))

        return resp
