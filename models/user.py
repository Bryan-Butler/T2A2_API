from main import db
from datetime import datetime
from sqlalchemy import DateTime

class User():
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    registration_date = db.Column(DateTime, default=datetime.utcnow())
    is_admin = db.Column(db.Boolean, default=False)

    # Define one-to-many relationships
    user_library = db.relationship("User_Library", back_populates="user")
    transactions = db.relationship("Transactions", back_populates="user")
    reviews = db.relationship("Reviews", back_populates="user")