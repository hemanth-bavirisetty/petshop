from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models import Pet

bp = Blueprint("pets", __name__, url_prefix="/api/pets")


@bp.get("")
def list_pets():
    return jsonify([p.to_dict() for p in Pet.query.all()])


@bp.get("/<int:pet_id>")
def get_pet(pet_id):
    pet = db.get_or_404(Pet, pet_id)
    return jsonify(pet.to_dict())


@bp.post("")
def create_pet():
    data = request.get_json(force=True)
    pet = Pet(
        name=data["name"],
        species=data["species"],
        breed=data.get("breed"),
        price=float(data["price"]),
        stock=int(data.get("stock", 1)),
    )
    db.session.add(pet)
    db.session.commit()
    return jsonify(pet.to_dict()), 201


@bp.delete("/<int:pet_id>")
def delete_pet(pet_id):
    pet = db.get_or_404(Pet, pet_id)
    db.session.delete(pet)
    db.session.commit()
    return "", 204