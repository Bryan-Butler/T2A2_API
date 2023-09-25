from main import db
from sqlalchemy import DateTime

class Game():
    __tablename__ = 'Game'

    GameID = db.Column(db.Integer, primary_key=True)
    GenreID = db.Column(db.Integer, db.ForeignKey('Genre.GenreID'))
    DeveloperID = db.Column(db.Integer, db.ForeignKey('Developer.DeveloperID'))
    PublisherID = db.Column(db.Integer, db.ForeignKey('Publisher.PublisherID'))
    Title = db.Column(db.String)
    ReleaseDate = db.Column(DateTime)
    AvgUserRating = db.Column(db.Float)
    NumUserRating = db.Column(db.Integer)

    # Define many-to-one relationships
    genre =  db.relationship("Genre", back_populates="games")
    developer = db.relationship("Developer", back_populates="games")
    publisher = db.relationship("Publisher", back_populates="games")
    user_library = db.relationship("UserLibrary", back_populates="game")
    transactions = db.relationship("Transactions", back_populates="game")
    reviews = db.relationship("Reviews", back_populates="game")

  