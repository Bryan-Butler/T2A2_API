from main import db
from sqlalchemy import DateTime

class User():
    __tablename__ = 'users'

    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String)
    Email = db.Column(db.String)
    Password = db.Column(db.String)
    Registration_Date = db.Column(DateTime)
    Is_Admin = db.Column(db.Boolean, default=False)

    # Define one-to-many relationships
    user_library = db.relationship("User_Library", back_populates="user")
    transactions = db.relationship("Transactions", back_populates="user")
    reviews = db.relationship("Reviews", back_populates="user")