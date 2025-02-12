from flask import Blueprint, request, jsonify
from models import Train
from utils.db import db
from utils.security import admin_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/train", methods=["POST"])
@admin_required
def add_train():
    data = request.get_json()
    train = Train(name=data["name"], source=data["source"], destination=data["destination"], total_seats=data["seats"], available_seats=data["seats"])
    db.session.add(train)
    db.session.commit()
    return jsonify({"message": "Train added successfully"})