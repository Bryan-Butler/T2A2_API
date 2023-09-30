from main import db
from datetime import datetime
from sqlalchemy import DateTime



class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)

    # Define one-to-many relationships
    user_library = db.relationship("User_Library", back_populates="user")
    transactions = db.relationship("Transactions", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")