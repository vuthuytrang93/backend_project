from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import func

from main import db


class User(db.Model):

    __tablename__ = "user"
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(255), nullable=False)
    email = db.Column(String(255), nullable=False, unique=True)
    hashed_password = db.Column(String(80), nullable=False)
    created_time = db.Column(DateTime(timezone=True), default=datetime.now())
    updated_time = db.Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, name: str, email: str, hashed_password: str):
        """Init user object
        param : email
        return: user database-object
        """
        self.name = name
        self.email = email
        self.hashed_password = hashed_password

    def save_to_db(self):
        """
        Save user to database
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Delete a user from database
        """
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        """Retrieve user by id
        param : cls, id
        return: user database-object
        """
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        """Retrieve user by name
        param : cls, name
        return: user database-object
        """
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_email(cls, email: str):
        """Retrieve user by email
        param : cls, email
        return: user database-object
        """
        return cls.query.filter_by(email=email).first()
