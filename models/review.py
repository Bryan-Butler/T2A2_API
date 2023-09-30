from main import db
from sqlalchemy import DateTime, Text

class Review(db.Model):
    __tablename__ = 'review'

    Review_ID = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    rating = db.Column(db.Integer)
    review_description = db.Column(Text)
    review_date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="reviews")
    game = db.relationship("Game", back_populates="reviews")