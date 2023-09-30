from main import db
from datetime import datetime

class Review():
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="reviews")
    game = db.relationship("Game", back_populates="reviews")