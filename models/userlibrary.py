from main import db
from sqlalchemy import DateTime

class User_Library():
    __tablename__ = 'user librarys'

    UserLibrary_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.User_ID'))
    Game_ID = db.Column(db.Integer, db.ForeignKey('Game.Game_ID'))
    Purchase_Date = db.Column(DateTime)
    Play_Time = db.Column(db.Integer)
    Status = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="User_Library")
    game = db.relationship("Game", back_populates="User_Library")