from main.models.category import Category
from main.models.item import Item
from main.models.user import User


def test_item_table(session):
    user = User("Becky", "beck@got-it.ai", "hashed_pass2")
    user.save_to_db()
    author_id = session.query(User).filter_by(name="Becky").first().id
    category = Category("Book", author_id)
    category.save_to_db()
    category_id = session.query(Category).filter_by(name="Book").first().id
    item = Item("Pride","A history book", author_id, category_id)
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
    item = Item("Pride","A history book", author_id, category_id)
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
    item = Item("Pride", "A history book", author_id, category_id)
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
    item = Item("Pride","A history book", author_id, category_id)
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
    item = Item("Pride","A history book", author_id, category_id)
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
    item = Item("Pride", "A history book",author_id, category_id)
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
    item1 = Item("Pride","A history book", author_id, category_id)
    item1.save_to_db()
    item2 = Item("Prejudice","A romance novel", author_id, category_id)
    item2.save_to_db()
    result = Item.find_all()
    expected = session.query(Item).all()
    assert result == expected
