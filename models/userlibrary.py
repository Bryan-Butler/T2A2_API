from main import db
from sqlalchemy import DateTime

class User_Library():
    __tablename__ = 'user librarys'

    user_library_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.game_id'))
    purchase_date = db.Column(DateTime)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="User_Library")
    game = db.relationship("Game", back_populates="User_Library")