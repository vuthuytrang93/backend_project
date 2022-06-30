from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from main import db
from main.models.category import Category
from main.models.user import User


class Item(db.Model):

    """
    Init Item db
    """

    __tablename__ = "item"
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), nullable=False)
    author_id = db.Column(Integer, ForeignKey("user.id"))
    category_id = db.Column(Integer, ForeignKey("category.id"))
    created_time = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_time = db.Column(DateTime(timezone=True), onupdate=func.now())

    author = relationship(User)  # Create relationship between an item & author
    category = relationship(Category)  # Create relationship between an item & category

    def __init__(self, name: str, author_id: int, category_id: int):
        """Init user object
        param : email
        return: user database-object
        """
        self.name = name
        self.author_id = author_id
        self.category_id = category_id

    def save_to_db(self):
        """
        Save an item to database
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Delete an item from database
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Retrieve an item by id
        param : cls, id
        return: ItemModel instance
        """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        """Retrieve an item  by name
        param : cls, name
        return: ItemModel instance
        """
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_category(cls, category_id):
        """Retrieve all items in a category
        param : cls, category_id
        return:ItemModelList
        """
        return cls.query.filter_by(category_id=category_id)

    @classmethod
    def find_by_author(cls, author_id):
        """Retrieve all items by an user
        param : cls, author
        return: CategoryModelList
        """
        return cls.query.filter_by(author_id=author_id)

    @classmethod
    def find_all(cls):
        """Retrieve all items
        param : cls
        return: ItemModelList
        """
        return cls.query.all()
