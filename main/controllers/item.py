from main import app
from main.engines.item import *
from main.libs.authenticate import *
from main.schemas.item import *


@app.route("/items", methods=["POST"])
@token_required
def create_item_controller(current_user):
    data = request.get_json(force=True)
    schema1 = ItemCreateSchema()
    try:
        data = schema1.load(data)
    except ValueError as err:
        return jsonify(err.messages), 400
    author_id = data["author_id"]
    if current_user.id == author_id:
        category = create_item(**data)
        schema2 = ItemInfoSchema()
        return schema2.dump(category), 200
    else:
        return jsonify({"message": "Unauthorized user. Login to create item"}), 403


@app.route("/items", methods=["GET"])
def get_items_controller():
    items = Item.find_all()
    schemas = ItemInfoSchema(many=True)
    return jsonify(schemas.dump(items)), 200


@app.route("/items/item", methods=["GET"])
def get_item_controller():
    data = request.args
    _id = data.get("item_id")
    item = get_item(_id)
    schemas = ItemInfoSchema()
    return jsonify(schemas.dump(item)), 200


@app.route("/items/author", methods=["GET"])
def get_item_author_controller():
    data = request.args
    _id = data.get("author_id")
    items = get_author_item_list(_id)
    schemas = ItemInfoSchema(many=True)
    return jsonify(schemas.dump(items)), 200


@app.route("/items/category", methods=["GET"])
def get_item_category_controller():
    data = request.args
    _id = data.get("category_id")
    items = get_category_item_list(_id)
    schemas = ItemInfoSchema(many=True)
    return jsonify(schemas.dump(items)), 200


# @app.route("/items/category", methods=["PUT"])
# @token_required
# def update_item_category_controller(current_user):
#     data = request.get_json(force=True)
#     schema1 = ItemUpdateCategorySchema()
#     try:
#         data = schema1.load(data)
#     except ValidationError as err:
#         return jsonify(err.messages), 400
#     author_id, category_id, item_id = data['author_id'], data['category_id'], data['item_id']
#     if author_id == current_user.id:
#         try:
#             update_item_category(author_id, category_id, item_id,)
#             return jsonify({"message": "Item is updated"}), 200
#         except ValidationError as err:
#             return jsonify(err.messages), 400


@app.route("/items/description", methods=["PUT"])
@token_required
def update_item_description_controller(current_user):
    data = request.get_json(force=True)
    schema1 = ItemUpdateDescriptionSchema()
    try:
        data = schema1.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    author_id, item_id, description = (
        data["author_id"],
        data["item_id"],
        data["description"],
    )
    if author_id == current_user.id:
        try:
            update_item_description(author_id, item_id, description)
            return jsonify({"message": "Item is updated"}), 200
        except ValidationError as err:
            return jsonify(err.messages), 400


@app.route("/items", methods=["DELETE"])
@token_required
def del_item_controller(current_user):
    data = request.get_json(force=True)
    schema1 = ItemDeleteSchema()
    try:
        data = schema1.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    author_id, category_id, item_id = (
        data["author_id"],
        data["category_id"],
        data["item_id"],
    )
    category = Category.find_by_id(category_id)
    if category is None:
        return jsonify({"message": "Category not found"}), 404
    if current_user.id != author_id:
        return (
            jsonify({"message": "Unauthorized user. Only author can delete category"}),
            403,
        )
    if current_user.id == author_id:
        delete_item(item_id)
        return jsonify({"message": "Item is deleted"}), 200
