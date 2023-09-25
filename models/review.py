from main import db
from sqlalchemy import DateTime, Text

class Reviews():
    __tablename__ = 'reviews'

    Review_ID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    GameID = db.Column(db.Integer, db.ForeignKey('Game.GameID'))
    Rating = db.Column(db.Integer)
    Review_Description = db.Column(Text)
    Review_Date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="reviews")
    game = db.relationship("Game", back_populates="reviews")