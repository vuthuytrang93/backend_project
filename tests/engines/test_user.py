from main.models.category import Category
from main.models.item import Item
from main.models.user import User
from main.engines.user import *


def test_get_user_info(session):
    user = User("John", "john@got-it.ai", "hashed_pass1")
    session.add(user)
    session.commit()
    expected = get_user_info(1)
    result = session.query(User).filter_by(id=1).first()
    assert result == expected


def test_check_user_exist(session):
    email = "john@got-it.ai"
    user = User("John", email, "hashed_pass1")
    user_existence_1 = check_user_exist(email)
    assert (user_existence_1 is False)
    session.add(user)
    session.commit()
    user_existence_2 = check_user_exist(email)
    assert (user_existence_2 is True)


def test_create_user(session):
    user = create_user("Becky", "beck@got-it.ai", "hashed_pass2")
    session.add(user)
    session.commit()
    user = User.find_by_email("beck@got-it.ai")
    assert user is not None


def test_digest_password():
    password = "Johnny"
    digested = hash_password(password)
    assert (type(digested) == type("") and digested != password)


def test_check_hashed_password():
    password = 'password1'
    wrong_input = 'dummypass'
    hashed = hash_password(password)
    result1 = check_hashed_password(password,hashed)
    result2 = check_hashed_password(wrong_input,hashed)
    assert (result1 is True and result2 is False)


def test_authenticate_user(session):
    right_pass = "foxunxxinf124@#$"
    wrong_pass = "foxxxinf124*9"
    create_user("Becky", "beck@got-it.ai", right_pass)
    user = session.query(User).filter_by(name="Becky")
    result1 = verify_user("beck@got-it.ai", right_pass)
    result2 = verify_user("beck@got-it.ai", wrong_pass)
    assert (result1 is True and result2 is False)

