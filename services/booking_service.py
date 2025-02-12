# railway_management/services/booking_service.py
from models import Train, Booking
from utils.db import db
from flask_jwt_extended import get_jwt_identity

class BookingService:
    @staticmethod
    def book_seat(train_id):
        train = Train.query.get(train_id)
        if train and train.available_seats > 0:
            train.available_seats -= 1
            booking = Booking(user_id=get_jwt_identity()["id"], train_id=train.id)
            db.session.add(booking)
            db.session.commit()
            return {"message": "Booking successful"}
        return {"message": "No seats available"}, 400
