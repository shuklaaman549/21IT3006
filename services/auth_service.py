# railway_management/services/auth_service.py
from models import User
from utils.db import db

class AuthService:
    @staticmethod
    def register_user(username, password):
        if User.query.filter_by(username=username).first():
            return {"message": "User already exists"}, 400
        
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully"}

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return {"token": user.generate_token()}
        return {"message": "Invalid credentials"}, 401
