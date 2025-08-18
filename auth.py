from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
# from src.api.controllers.auth import Auth
from src.db.core import db

# Create blueprint for auth routes
auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

class AuthList(Resource):
    def post(self):
        """Authenticate user"""
        # data = request.get_json()
        return {"message": "created successful"}, 201
        # if not data or 'username' not in data or 'password' not in data:
        #     return {"message": "Please provide username and password"}, 400
        
        # auth = auth.query.filter_by(name=data['username']).first()
        # if not auth or not auth.check_password(data['password']):
        #     return {"message": "Invalid username or password"}, 401
        
        # # Assuming you have a method to generate tokens
        # token = auth.generate_auth_token()
        
    # , "token": token

api.add_resource(AuthList, '/auth')