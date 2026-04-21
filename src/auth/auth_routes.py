from flask import Blueprint, request, jsonify
from src.auth.jwt_utils import create_token
from src.models.player import Player

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "username required"}), 400

    user = Player.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error": "user not found"}), 404

    token = create_token(user.id)

    return jsonify({
        "token": token
    })