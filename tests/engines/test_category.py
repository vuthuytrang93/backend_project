from main.models.category import Category
from main.models.item import Item
from main.models.user import User
from main.engines.user import *
from main.engines.category import *


def test_create_category(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_name("Becky")
    author_id = user.id
    category = create_category("Book", author_id)
    result = session.query(Category).filter_by(name="Book").first()
    assert result is not None


def test_get_one_category(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    category_data = session.query(Category).filter_by(name="Book").first()
    expected = session.query(Category).filter_by(id=category_data.id).first()
    result = get_one_category(category_data.id)
    assert result == expected


def test_get_many_categories(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category1 = Category("Book", author_id)
    category1.save_to_db()
    category2 = Category("Coffee", author_id)
    category2.save_to_db()
    expected = get_many_categories(author_id)
    result = session.query(Category).filter_by(author_id=author_id).all()
    assert result == expected


def test_delete_category(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    delete_category(author_id, category.id)
    result = session.query(Category).filter_by(name="Book").first()
    assert result is None


