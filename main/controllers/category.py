
from main.engines.category import *
from main.libs.authenticate import *
from main.schemas.category import *
from marshmallow import ValidationError


from main import app


@app.route('/categories', methods=['POST'])
@token_required
def create_category_controller(current_user):
    """
    Create a category
    """
    data = request.get_json(force=True)
    try:
        data = AuthorCategorySchema().load(data)
    except ValidationError:
        return jsonify({"error":"Wrong request format"}),400
    author_id = data['author_id']
    if current_user.id == author_id:
        category = create_category(**data)
        return  CategoryInfoSchema().dump(category), 200
    else:
        return jsonify({'message': 'Forbidden. Login to create category'}), 403

# Implement ca
@app.route('/categories', methods=['GET'])
def get_categories_controller():
    categories = Category.find_all()
    schema = CategoryInfoSchema()
    try:
        return schema.jsonify(categories, many=True), 200
    except (ValidationError, ValueError, LookupError):
        return jsonify({"error": "Categories cannot be found"}), 400


@app.route('/categories/author', methods=['GET'])
def get_categories_author_controller():
    """
    Get list of all categories by a user
    """
    data = request.args
    _id = data.get('author_id')
    categories = get_many_categories(_id)
    schemas = CategoryInfoSchema(many=True)
    if len(categories) != 0:
        return jsonify(schemas.dump(categories)), 200
    else:
        return jsonify({"messages": "Items list is empty"}), 200


@app.route('/categories/category', methods=['GET'])
def get_category_controller():
    """
    Get one category
    """
    data = request.args
    _id = data.get('category_id')
    category = get_one_category(_id)
    schemas2 = CategoryInfoSchema()
    return schemas2.dump(category), 200


@app.route('/categories', methods=['DELETE'])  # delete a category
@token_required
def del_category_controller(current_user):
    """
    Delete a category
    """
    data = request.get_json(force=True)
    schema1 = AuthorCategoryIdSchema()
    try:
        data = schema1.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    author_id, category_id = data['author_id'], data['category_id']
    if current_user.id == author_id:
        delete_category(author_id, category_id)
        return jsonify({'message': 'Category is deleted'}), 200
    else:
        return jsonify({'message': 'Unauthorized user. Only author can delete category'}), 403
