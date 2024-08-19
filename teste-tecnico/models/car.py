import enum
from database import db


class CarColor(enum.Enum):
    blue = "blue"
    yellow = "yellow"
    gray = "gray"


class CarModel(enum.Enum):
    hatch = "hatch"
    sedan = "sedan"
    convertible = "convertible"


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    color = db.Column(db.Enum(CarColor))
    model = db.Column(db.Enum(CarModel))
    id_owner = db.Column(db.Integer, db.ForeignKey("owner.id"))

    def __init__(self, color, model, id_owner):
        self.color = color
        self.model = model
        self.id_owner = id_owner


def getCarsForOwnersById(id):
    owners_cars = Car.query.filter_by(id_owner=id).all()
    carsArr = []
    for car in owners_cars:
        carsArr.append({
            "id": car.id,
            "color": car.color.value,
            "model": car.model.value,
            "id_owner": car.id_owner
        })
    return carsArr