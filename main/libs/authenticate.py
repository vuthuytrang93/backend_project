from functools import wraps

import jwt
from flask import jsonify, request

from main import app
from main.models.user import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.find_by_id(data["id"])
            if current_user is None:
                return jsonify({"message": "Wrong login info"}), 401
        except Exception:
            return jsonify({"message": "Token is invalid !!"}), 401
        return f(current_user, *args, **kwargs)

    return decorated
