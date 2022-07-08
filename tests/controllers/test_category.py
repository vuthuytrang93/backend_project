from main.controllers.user import *
from main.controllers.category import *


# def test_create_category(client):
#     create_user(name="Joe", email="joe@joes.com", password="123456")
#     response = client.post('categories', json={"name": "Book", "author_id": 1})
#     assert response.status_code ==200


def test_get_categories(client, session):
    create_user(name="Joe", email="joe@joes.com", password="123456")
    _id = session.query(User).filter_by(name="Joe").first().id
    create_category(name="Book", author_id=_id)
    response = client.get('/categories', json={"category_id": 1})
    assert response.status_code == 200

# def test_get_category(client, session):
#     create_user(name="Joe", email="joe@joes.com", password="123456")
#     _id = session.query(User).filter_by(name="Joe").first().id
#     create_category(name="Book", author_id=_id)
#     response = client.get('/categories/categories', json={"category_id": 1})
#     assert response.status_code == 200


# def test_get_category_author(client,session):
#     create_user(name="Joe", email="joe@joes.com", password="123456")
#     _id = session.query(User).filter_by(name="Joe").first().id
#     create_category(name="Book", author_id=_id)
#     create_category(name="Coffee", author_id=_id)
#     response = client.get("/categories/author?author_id=1")
#     assert response.status_code == 200