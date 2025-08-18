from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
from flask import Blueprint
from src.db.model.user import User
from src.db.core import db
from werkzeug.security import generate_password_hash

#create blueprints for section routes

users_bp = Blueprint('users', __name__)
api = Api(users_bp)

# user_paser for posting
user_paser = reqparse.RequestParser()
user_paser.add_argument('first_name', type=str, nullable=False, help='First name is required')
user_paser.add_argument('last_name', type=str, nullable=False, help='Last name is required') 
user_paser.add_argument('email', type=str, nullable=False, help='Email is required')
user_paser.add_argument('phone', type=str, nullable=True, help='Phone number is optional')
user_paser.add_argument('address', type=str, nullable=True, help='Address is optional')
user_paser.add_argument('password', type=str, nullable=False, help='Password is required')
user_paser.add_argument('roll', type=str, choices=['USER', 'MODERATOR', 'ADMIN', 'SUPER_ADMIN'], default='USER')

# user_paser for updating

updateUserparser = reqparse.RequestParser()
updateUserparser.add_argument('first_name required', type=str)
updateUserparser.add_argument('last_name required', type=str)

class userList(Resource):
    def get(self):
        # get all users
        users= User.query.all()
        if not users:
            return ("message: no user found")
        users_list = []
        for user in users:
            users_list.append ({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email':user.email,
                'address': user.address,
                'roll':user.roll.name,
                'phone': user.phone
            })
        return jsonify({"users":users_list})
            

    def post(self):
        #create New sections
        args =user_paser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        new_user= User (
            first_name= args['first_name'],
            last_name=args['last_name'],
            email= args['email'],
            phone = args['phone'],
            address = args['address'],
            password = hashed_password,
            roll = args['roll']
        )
        
        if User.query.filter_by(email=new_user.email).first():
            return {'message': 'user already exists'}, 400
        
        db.session.add(new_user)
        db.session.commit()

        return ({'message': 'creating record is successful', 'user':{"id":new_user.id, "firstname": new_user.first_name}}), 201
    

class userResource(Resource):
    def get(self,user_id):
        users=User.query.get(user_id)
        if not users:
            return ({'message':'user not found'}),404
        
        users_data ={
                'id': users.id,
                'first_name': users.first_name,
                'last_name': users.last_name,
                'email':users.email,
                'address': users.address,
                'roll':users.roll.name,
                'phone': users.phone
            }
        return jsonify({"users":users_data})
        
    
    
    def put (self,user_id):
        args =user_paser.parse_args()
        new_user= User (
            first_name= args['first_name'],
            last_name=args['last_name'],
            email= args['email'],
            phone = args['phone'],
            address = args['address'],
            roll = args['roll']
        )

        if User.query.filter_by(email=new_user.email).first():
            return {'message': 'user already exists'}, 400
        
        db.session.add(new_user)
        db.session.commit()
        return ({'message': ' record is successfully updated', 'user':{"id":user_id, "firstname": new_user.first_name}}), 201
    
    
    
    def delete(self,user_id):
        users = User.query.get(user_id) 
        if not users:
            return ({'message':'user not exist'}),404
        db.session.delete(users)
        db.session.commit()
        return jsonify({'message':'user deleted successfully'}), 200
        

        
api.add_resource(userList, '/users')

api.add_resource( userResource, '/users/<int:user_id>')

