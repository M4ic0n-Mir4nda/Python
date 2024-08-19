import os
from flask import Flask, request, jsonify
from database import db
from models.car import CarColor, CarModel, Car, getCarsForOwnersById
from models.owner import Owner, isOwner, getOwners


def create_app(config_type='default'):
    app = Flask(__name__)

    if config_type == 'testing':
        app.config['SECRET_KEY'] = 'test_secret_key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        db_name = os.getenv("MYSQL_DATABASE")
        secret_key = os.getenv("SECRET_KEY")
        connection = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
        app.config["SQLALCHEMY_DATABASE_URI"] = connection
        app.config['SECRET_KEY'] = secret_key

    db.init_app(app)

    @app.route("/owner", methods=["POST"])
    def createOwner():
        obj = request.get_json()
        if not "name" in obj:
            return {"message": "Field name must be not null."}, 402
        owner_created = Owner(obj["name"])
        db.session.add(owner_created)
        db.session.commit()
        return jsonify({
            "id": owner_created.id,
            "name": owner_created.name
        }), 201

    @app.route("/owner", methods=["GET"])
    def getAllOwners():
        owners = getOwners()
        return jsonify(owners), 200

    @app.route("/cars", methods=["POST"])
    def createCarForOwners():
        obj = request.get_json()
        if not "color" in obj or obj["color"] not in CarColor._value2member_map_:
            return {"message": "Value null or missing color."}, 402
        if not "model" in obj or obj["model"] not in CarModel._value2member_map_:
            return {"message": "Value null or missing model."}, 402
        if not "id_owner" in obj:
            return {"message": "Field id_owner must be not null."}, 402
        if not isOwner(obj["id_owner"]):
            return {"message": "Owner not found. Car cannot exist without an owner."}, 404
        if len(getCarsForOwnersById(obj["id_owner"])) == 3:
            return {"message": "You can only have up to 3 cars."}, 402
        car_for_owner = Car(
            color=CarColor(obj["color"]),
            model=CarModel(obj["model"]),
            id_owner=obj["id_owner"]
        )
        db.session.add(car_for_owner)
        db.session.commit()
        return jsonify({
            "id": car_for_owner.id,
            "color": car_for_owner.color.value,
            "model": car_for_owner.model.value,
            "id_owner": car_for_owner.id_owner
        }), 201

    @app.route("/cars/<int:id>", methods=["GET"])
    def getAllCarsForOwner(id):
        owners_cars = getCarsForOwnersById(id)
        return jsonify(owners_cars)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)
