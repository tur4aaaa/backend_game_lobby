from src.auth.jwt_utils import verify_token
from flask import request, jsonify
from functools import wraps


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"error": "No token found"}), 401

        try:
            token = auth_header.split(" ")[1]
        except Exception:
            return jsonify({"error": "Invalid token format"}), 401

        user_id = verify_token(token)

        if not user_id:
            return jsonify({"error": "Invalid or expired token"}), 403

        request.user_id = user_id

        return func(*args, **kwargs)

    return wrapper