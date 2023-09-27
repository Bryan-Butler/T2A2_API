from main import db
from sqlalchemy import DateTime

class Game():
    __tablename__ = 'games'

    Game_ID = db.Column(db.Integer, primary_key=True)
    Genre_ID = db.Column(db.Integer, db.ForeignKey('Genre.Genre_ID'))
    Developer_ID = db.Column(db.Integer, db.ForeignKey('Developer.Developer_ID'))
    Publisher_ID = db.Column(db.Integer, db.ForeignKey('Publisher.Publisher_ID'))
    Title = db.Column(db.String)
    Release_Date = db.Column(DateTime)
    Avg_User_Rating = db.Column(db.Float)
    Num_User_Rating = db.Column(db.Integer)

    # Define many-to-one relationships
    genre =  db.relationship("Genre", back_populates="games")
    developer = db.relationship("Developer", back_populates="games")
    publisher = db.relationship("Publisher", back_populates="games")
    user_library = db.relationship("User_Library", back_populates="games")
    transactions = db.relationship("Transactions", back_populates="games")
    reviews = db.relationship("Reviews", back_populates="games")

  