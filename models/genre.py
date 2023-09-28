from main import db

class Genre():
    __tablename__ = 'genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String)

    games = db.relationship("Game", back_populates="genre")