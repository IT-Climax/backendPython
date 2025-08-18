from src.db.core import db
from enum import Enum
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
import datetime


class Role(Enum):
    USER = 0
    MODERATOR = 1
    ADMIN = 2
    SUPER_ADMIN = 3


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone =  db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(128))
    role = db.Column(db.Enum(Role), default=Role.USER)


    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User{self.email}>'
    

