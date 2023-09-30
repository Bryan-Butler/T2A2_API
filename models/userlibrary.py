from main import db
from sqlalchemy import DateTime

class User_Library(db.Model):
    __tablename__ = 'user_library'

    user_library_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    purchase_date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="user_library")
    game = db.relationship("Game", back_populates="user_library")