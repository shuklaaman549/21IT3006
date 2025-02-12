from flask import request, jsonify
from config import Config
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get("API-Key") != Config.ADMIN_API_KEY:
            return jsonify({"message": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function

def jwt_required_role(required_admin=False):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            verify_jwt_in_request()
            user = get_jwt_identity()
            if required_admin and not user.get("is_admin"):
                return jsonify({"message": "Admin access required"}), 403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper