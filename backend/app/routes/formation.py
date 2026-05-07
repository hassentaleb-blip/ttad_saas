from flask import Blueprint, request, jsonify
from app.models import Formation
from app import db

formation_bp = Blueprint("formation", __name__)

@formation_bp.route("/", methods=["GET"])
def get_all():
    formations = Formation.query.all()
    return jsonify([
        {"id": f.id, "title": f.title, "price": f.price}
        for f in formations
    ])

@formation_bp.route("/", methods=["POST"])
def create():
    data = request.json

    f = Formation(
        title=data["title"],
        description=data["description"],
        price=data["price"]
    )

    db.session.add(f)
    db.session.commit()

    return jsonify({"msg": "Formation added"})