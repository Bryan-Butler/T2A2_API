from main import db
from sqlalchemy import DateTime, Text

class Review():
    __tablename__ = 'reviews'

    Review_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.User_ID'))
    Game_ID = db.Column(db.Integer, db.ForeignKey('Game.Game_ID'))
    Rating = db.Column(db.Integer)
    Review_Description = db.Column(Text)
    Review_Date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="reviews")
    game = db.relationship("Game", back_populates="reviews")