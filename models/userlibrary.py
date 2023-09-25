from main import db
from sqlalchemy import DateTime

class UserLibrary():
    __tablename__ = 'UserLibrary'

    UserLibraryID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    GameID = db.Column(db.Integer, db.ForeignKey('Game.GameID'))
    PurchaseDate = db.Column(DateTime)
    Playtime = db.Column(db.Integer)
    Status = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="user_library")
    game = db.relationship("Game", back_populates="user_library")