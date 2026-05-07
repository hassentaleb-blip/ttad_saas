from flask import Blueprint, request, jsonify
from ..models import db, Formation
from flask_jwt_extended import jwt_required
formations_bp = Blueprint("formations", __name__)

# CREATE
@formations_bp.route("/", methods=["POST"])
def create_formation():
    data = request.json

    formation = Formation(
        title=data["title"],
        description=data["description"],
        price=data["price"]
    )

    db.session.add(formation)
    db.session.commit()

    return jsonify({"message": "Formation created"}), 201


# GET ALL
@formations_bp.route("/", methods=["GET"])
def get_formations():
    formations = Formation.query.all()

    result = []
    for f in formations:
        result.append({
            "id": f.id,
            "title": f.title,
            "description": f.description,
            "price": f.price
        })

    return jsonify(result)


# DELETE
@formations_bp.route("/<int:id>", methods=["DELETE"])
def delete_formation(id):
    formation = Formation.query.get(id)

    if not formation:
        return jsonify({"message": "Not found"}), 404

    db.session.delete(formation)
    db.session.commit()

    return jsonify({"message": "Deleted"})