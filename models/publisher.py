from main import db

class Publisher():
    __tablename__ = 'publishers'

    Publisher_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Website = db.Column(db.String)
    Contact_info = db.Column(db.String)

    games = db.relationship("Game", back_populates="publisher")