from main.models.category import Category
from main.models.item import Item
from main.models.user import User


def test_user_table(session):
    user = User("John", "john@got-it.ai", "hashed_pass1")
    session.add(user)
    session.commit()
    expected = user
    result = session.query(User).first()
    assert result == expected


def test_user_save(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    expected = user
    result = session.query(User).filter_by(name="Becky").first()
    assert result == expected


def test_user_find_by_name(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    expected = session.query(User).filter_by(name="Becky").first()
    result = User.find_by_name("Becky")
    assert result == expected


def test_user_find_by_id(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    expected = session.query(User).filter_by(id=1).first()
    result = User.find_by_id(1)
    assert result == expected


def test_user_find_by_email(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    expected = session.query(User).filter_by(email="john@got-it.ai").first()
    result = User.find_by_email("john@got-it.ai")
    assert result == expected


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


def test_item_table(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    session.add(item)
    session.commit()
    result = session.query(Item).first()
    assert result == item


def test_item_save(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    item.save_to_db()
    result = session.query(Item).first()
    assert result == item


def test_item_del(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    item.save_to_db()
    item.delete_from_db()
    result = session.query(Item).first()
    assert result is None


def test_item_find_by_name(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    item.save_to_db()
    result = Item.find_by_name("Pride")
    expected = session.query(Item).filter_by(name="Pride").first()
    assert result == expected


def test_item_find_by_id(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    item.save_to_db()
    item_id = session.query(Item).filter_by(name="Pride").first().id
    result = Item.find_by_id(item_id)
    expected = session.query(Item).filter_by(id=item_id).first()
    assert result == expected


def test_item_find_by_author(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride", author_id, category_id)
    item.save_to_db()
    result = Item.find_by_author(author_id).first()
    expected = session.query(Item).filter_by(author_id=author_id).first()
    assert result == expected


def test_item_find_all(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item1 = Item("Pride", author_id, category_id)
    item1.save_to_db()
    item2 = Item("Prejudice", author_id, category_id)
    item2.save_to_db()
    result = Item.find_all()
    expected = session.query(Item).all()
    assert result == expected
