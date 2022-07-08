from main.models.category import Category
from main.models.user import User


def test_category_table(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    session.add(category)
    session.commit()
    expected = category
    result = session.query(Category).first()
    assert result == expected


def test_category_save(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    category.save_to_db()
    expected = category
    result = session.query(Category).first()
    assert result == expected


def test_category_del(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    category.save_to_db()
    category.delete_from_db()
    result = session.query(Category).first()
    assert result is None


def test_category_find_by_name(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    category.save_to_db()
    expected = Category.find_by_name("Book")
    result = session.query(Category).filter_by(name="Book").first()
    assert result == expected


def test_category_find_by_id(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    category.save_to_db()
    expected = Category.find_by_id(1)
    result = session.query(Category).filter_by(id=1).first()
    assert result == expected


def test_category_find_by_author(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category = Category("Book", author_id)
    category.save_to_db()
    expected = Category.find_by_author(1).first()
    result = session.query(Category).filter_by(author_id=1).first()
    assert result == expected


def test_category_find_all(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    user_data = session.query(User).filter_by(name="Becky").first()
    author_id = user_data.id
    category1 = Category("Book", author_id)
    category1.save_to_db()
    category2 = Category("Coffee", author_id)
    category2.save_to_db()
    expected = Category.find_all()
    result = session.query(Category).all()
    assert result == expected
