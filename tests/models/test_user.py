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
