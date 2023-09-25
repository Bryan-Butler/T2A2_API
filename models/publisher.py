from main import db

class Publisher():
    __tablename__ = 'Publisher'

    PublisherID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Website = db.Column(db.String)
    Contactinfo = db.Column(db.String)

    games = db.relationship("Game", back_populates="publisher")