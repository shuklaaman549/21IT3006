# railway_management/services/train_service.py
from models import Train
from utils.db import db

class TrainService:
    @staticmethod
    def add_train(name, source, destination, seats):
        train = Train(name=name, source=source, destination=destination, total_seats=seats, available_seats=seats)
        db.session.add(train)
        db.session.commit()
        return {"message": "Train added successfully"}

    @staticmethod
    def get_trains(source, destination):
        trains = Train.query.filter_by(source=source, destination=destination).all()
        return [{"id": train.id, "name": train.name, "available_seats": train.available_seats} for train in trains]
