from main.models.category import Category
from main.models.item import Item
from main.models.user import User


def create_category(name: str, author_id: int) -> Category:
    category = Category.find_by_name(name)
    if category is not None:
        raise LookupError("Category already exists")
    else:
        new_category = Category(name, author_id)
        new_category.save_to_db()
        category = Category.find_by_name(name)
    return category


def get_one_category(category_id: int) -> Category:
    category = Category.find_by_id(category_id)
    if category is None:
        raise LookupError("Category not found")
    return category


def get_many_categories(author_id: int):
    author = User.find_by_id(author_id)
    if author is None:
        raise LookupError("Author not found")
    category = Category.find_by_author(author_id).all()
    if category is None:
        raise LookupError("Category not found")
    else:
        return category


def delete_category(author_id: int, category_id: int) -> None:
    category = Category.find_by_id(category_id)
    if category is None:
        raise LookupError("Category not found")
    elif category.author_id != author_id:
        raise ValueError("Forbidden. Only author can delete category")
    else:
        items = Item.find_by_category(category_id).all()
        for item in items:
            item.delete_from_db()
        category.delete_from_db()
