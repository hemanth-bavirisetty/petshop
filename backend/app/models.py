from .extensions import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(40), nullable=False)
    breed = db.Column(db.String(80))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=1)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "price": self.price,
            "stock": self.stock,
        }