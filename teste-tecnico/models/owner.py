from database import db


class Owner(db.Model):
    __tablename__ = "owner"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


def isOwner(id):
    return Owner.query.filter_by(id=id).first()


def getOwners():
    owners = Owner.query.all()
    ownerArr = []
    for owner in owners:
        ownerArr.append({
            "id": owner.id,
            "name": owner.name
        })
    return ownerArr