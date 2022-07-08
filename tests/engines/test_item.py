from main.models.category import Category
from main.models.item import Item
from main.models.user import User
from main.engines.user import *
from main.engines.category import *
from main.engines.item import *


def test_create_item(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    expected = create_item("Pride and Prejudice", "A romance novel", author_id, category_id)
    result = session.query(Item).filter_by(name="Pride and Prejudice").first()
    assert result == expected


def test_get_item(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride and Prejudice", "A romance novel", author_id, category_id)
    session.add(item)
    session.commit()
    item_id = session.query(Item).filter_by(name="Pride and Prejudice").first().id
    expected = get_item(item_id)
    result = session.query(Item).filter_by(id=item_id).first()
    assert result == expected


def test_get_category_item_list(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride and Prejudice", "A romance novel", author_id, category_id)
    session.add(item)
    session.commit()
    expected = get_category_item_list(category_id)
    result = session.query(Item).filter_by(category_id=category_id).all()
    assert result == expected


def test_get_author_item_list(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item1 = Item("Pride and Prejudice", "A romance novel", author_id, category_id)
    item2 = Item("Sapiens", "A book of revolution", author_id, category_id)
    session.add(item1, item2)
    session.commit()
    expected = get_author_item_list(author_id)
    result = session.query(Item).filter_by(author_id=author_id).all()
    assert result == expected


def tes_update_item(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride and Prejudice", "A romance novel", author_id, category_id)
    session.add(item)
    session.commit()
    item_data = session.query(Item).filter_by(author_id=author_id).first()
    update_item_description(item_data.id, author_id,"A new description")
    expected = "A new description"
    result = session.query(Item).filter_by(author_id=author_id).first().description
    assert result == expected


def test_delete_item(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride and Prejudice", "A romance novel", author_id, category_id)
    session.add(item)
    session.commit()
    item_data = session.query(Item).filter_by(name="Pride and Prejudice").first()
    assert item_data is not None
    delete_item(item_data.id)
    result = session.query(Item).filter_by(name="Pride and Prejudice").first()
    assert result is None


