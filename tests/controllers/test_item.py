from main.controllers.category import *
from main.controllers.item import *
from main.controllers.user import *


def test_get_item(client, session):
    create_user(name="Joe", email="joe@joes.com", password="123456")
    author_id = session.query(User).filter_by(name="Joe").first().id
    create_category(name="Book", author_id=author_id)
    category_id = session.query(Category).filter_by(name="Book").first().id
    create_item("Pride", "A novel", author_id, category_id)
    response = client.get("/items")
    assert response.status_code == 200


def test_get_item(client, session):
    create_user(name="Joe", email="joe@joes.com", password="123456")
    author_id = session.query(User).filter_by(name="Joe").first().id
    create_category(name="Book", author_id=author_id)
    category_id = session.query(Category).filter_by(name="Book").first().id
    create_item("Pride", "A novel", author_id, category_id)
    response = client.get("/items")
    assert response.status_code == 200
