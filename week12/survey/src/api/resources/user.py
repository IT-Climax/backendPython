from flask import request,jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.db.models.user import User
from src.db.core import db

#  create blueprint for users routes
users_bp = Blueprint('users',__name__)
api = Api(users_bp)

class UserList(Resource):
    def get(self):
        users = User.query.all()
        return {"users": [user.serialize() for user in users]}, 200
    

    def post(self):
        """create new section for user"""
        data = request.get_json()
        if not data or 'name' not in data:
            return {"message":"please insert a name"},400
        
        if User.query.filter_by(name=data['name']).first():
            return {"message":"user name already exists"},400
        
        new_user = User(name=data["name"])
        db.session.add(new_user)
        db.session.commit()
         

        return jsonify({"message": "creating record is successful", "user": new_user.serialize()}), 201
    
# to get all
class UserResource(Resource):
    """handle collection of sections"""
    def get(self, user_id):
        """retrieve a specific user by ID"""
        user = User.query.get(user_id)
        if not user:
            return {"message": "User not found"}, 404
        return jsonify(user.serialize())
    
# Register resources with distinct endpoints
api.add_resource(UserList, '/users')  
api.add_resource(UserResource, '/users/<int:user_id>')  