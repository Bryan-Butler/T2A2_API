from main import db
from sqlalchemy import DateTime

class Game(db.Model):
    __tablename__ = 'game'

    game_id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.developer_id'))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.publisher_id'))
    title = db.Column(db.String)
    release_date = db.Column(DateTime)
    avg_user_rating = db.Column(db.Float)
    num_user_rating = db.Column(db.Integer)

    # Define many-to-one relationships
    genre = db.relationship("Genre", back_populates="games")
    developer = db.relationship("Developer", back_populates="games")
    publisher = db.relationship("Publisher", back_populates="games")
    user_library = db.relationship("User_Library", back_populates="game")
    transactions = db.relationship("Transactions", back_populates="game")
    reviews = db.relationship("Review", back_populates="game")