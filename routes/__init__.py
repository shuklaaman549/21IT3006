from flask import Blueprint

# Blueprint registration
auth_bp = Blueprint('auth', __name__)
admin_bp = Blueprint('admin', __name__)
user_bp = Blueprint('user', __name__)
