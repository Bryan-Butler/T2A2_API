from main import db
from sqlalchemy import DateTime

class user():
    __tablename__ = 'User'

    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String)
    Email = db.Column(db.String)
    Password = db.Column(db.String)
    RegistrationDate = db.Column(DateTime)

    # Define one-to-many relationships
    user_library = db.relationship("UserLibrary", back_populates="user")
    transactions = db.relationship("Transactions", back_populates="user")
    reviews = db.relationship("Reviews", back_populates="user")