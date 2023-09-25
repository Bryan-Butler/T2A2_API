from main import db

class Genre():
    __tablename__ = 'Genre'

    GenreID = db.Column(db.Integer, primary_key=True)
    GenreName = db.Column(db.String)

    games = db.relationship("Game", back_populates="genre")