from main import db

class Genre():
    __tablename__ = 'genres'

    Genre_ID = db.Column(db.Integer, primary_key=True)
    Genre_Name = db.Column(db.String)

    games = db.relationship("Game", back_populates="genre")