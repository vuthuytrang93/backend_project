from main.models.item import Item
from main.models.category import Category
from main.models.user import User
from main.commons import exceptions


def create_item(name: str, description: str, author_id: int, category_id: int) -> Item:
    item = Item.find_by_name(name)
    category = Category.find_by_id(category_id)
    if item is not None:
        raise ValueError('Item already exists')
    elif category is None:
        raise LookupError('Category does not exists')
    else:
        new_item = Item(name, description, author_id, category_id)
        new_item.save_to_db()
        item = Item.find_by_name(name)
    return item


def get_item(item_id: int) -> Item:
    item = Item.find_by_id(item_id)
    if item is None:
        raise LookupError('Item not found')
    else:
        return item


def get_category_item_list(category_id: int):
    category = Category.find_by_id(category_id)
    if category is None:
        raise LookupError('Category not found')
    else:
        return Item.find_by_category(category_id).all()


def get_author_item_list(author_id: int):
    author = User.find_by_id(author_id)
    if author is None:
        raise LookupError('Author not found')
    else:
        return Item.find_by_author(author_id).all()


def update_item_description(item_id: int, author_id: int, description: str) -> None:
    item = Item.find_by_id(item_id)
    if item is None:
        raise LookupError('Item not found')
    elif item.author_id != author_id:
        raise ValueError('Unauthorized author')
    else:
        item.description = description
        item.save_to_db()


# def update_item_category (author_id: int, category_id: int, item_id: int) -> None:
#     item = Item.find_by_id(item_id)
#     category = Category.find_by_id(category_id)
#     if item is None:
#         raise LookupError('Item not found')
#     elif item.author_id != author_id:
#         raise ValueError('Unauthorized author')
#     else:
#         item.category_id = category_id
#         item.save_to_db()


def delete_item(item_id: int) -> None:
    item = Item.find_by_id(item_id)
    if item is None:
        raise LookupError('Item not found')
    else:
        item.delete_from_db()


