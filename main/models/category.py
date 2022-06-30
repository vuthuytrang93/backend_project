from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from main import db
from main.models.user import User


class Category(db.Model):

    """
    Init category db
    """

    __tablename__ = "category"
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), nullable=False)
    author_id = db.Column(Integer, ForeignKey("user.id"))  # Create foreign key
    created_time = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_time = db.Column(DateTime(timezone=True), onupdate=func.now())

    author = relationship(User)  # Create relationship between category and its author

    def __init__(self, name: str, author_id: int):
        """Init category object
        param : name, author_id
        return: category database-object
        """
        self.name = name
        self.author_id = author_id

    def save_to_db(self):
        """
        Save a category to database
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Delete a category from database
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        """Retrieve a category by id
        param : cls, id
        return: CategoryModel instance
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        """Retrieve a category by name
        param : cls, name
        return: CategoryModel instance
        """
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_author(cls, author_id):
        """Retrieve all categories by an user
        param : cls, author
        return: CategoryModelList
        """
        return cls.query.filter_by(author_id=author_id)

    @classmethod
    def find_all(cls):
        """Retrieve all categories
        param : cls, author
        return: CategoryModelList
        """
        return cls.query.all()
