from main import db
from sqlalchemy import DateTime, Text

class Review():
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.game_id'))
    rating = db.Column(db.Integer)
    review_description = db.Column(Text)
    revie_date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="reviews")
    game = db.relationship("Game", back_populates="reviews")