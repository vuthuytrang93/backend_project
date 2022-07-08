import jwt

from main import app
from main.engines.user import *
from main.libs.authenticate import *
from main.schemas.user import *


@app.route("/users", methods=["POST"])
def create_user_controller():
    data = request.get_json(force=True)
    user = create_user(**data)
    try:
        schema = UserInfoSchema()
        return schema.dump(user), 200
    except (ValidationError, LookupError, ValueError):
        return jsonify({"error": "User cannot be found"}), 400


@app.route("/users/me", methods=["GET"])
@token_required
def get_user_controller(current_user):
    schema = UserInfoSchema()
    return schema.dump(current_user), 200


@app.route("/login", methods=["POST"])
def login():
    login_schema = UserLogInSchema()
    info_schema = UserInfoSchema()
    data = request.get_json(force=True)
    try:
        input_data = login_schema.load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400
    user = User.find_by_email(input_data["email"])
    if not user:
        return jsonify({"error": "User does not exist"}), 400
    user_data = info_schema.dump(user)
    if verify_user(user_data["email"], input_data["password"]):
        token = jwt.encode(
            {"id": user_data["id"]}, app.config["SECRET_KEY"], algorithm="HS256"
        )
        return jsonify({"bearer": token}), 200
    else:
        raise ValidationError


#     use user object instead of schema
