from app import db


class Inform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zipCode = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    address = db.Column(db.String(128), index=True)


    def __init__(self, zipCode, lat, lng, address):
        self.zipCode = zipCode
        self.lat = lat
        self.lng = lng
        self.address = address