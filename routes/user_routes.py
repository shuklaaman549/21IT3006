from flask import Blueprint, request, jsonify
from models import Train, Booking
from utils.db import db
from utils.security import jwt_required_role

user_bp = Blueprint("user", __name__)

@user_bp.route("/trains", methods=["GET"])
def get_trains():
    source = request.args.get("source")
    destination = request.args.get("destination")
    trains = Train.query.filter_by(source=source, destination=destination).all()
    return jsonify([{ "name": train.name, "available_seats": train.available_seats } for train in trains])

@user_bp.route("/book", methods=["POST"])
@jwt_required_role()
def book_seat():
    data = request.get_json()
    train = Train.query.get(data["train_id"])
    if train and train.available_seats > 0:
        train.available_seats -= 1
        booking = Booking(user_id=get_jwt_identity()["id"], train_id=train.id)
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message": "Booking successful"})
    return jsonify({"message": "No seats available"}), 400