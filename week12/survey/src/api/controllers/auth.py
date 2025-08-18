from flask import request, jsonify
from flask_restful import Resource, Api
from flask import Blueprint
from src.db.models.user import Auth 
from src.db.core import db

# Create blueprint for auth routes
auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

Auth