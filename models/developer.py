from main import db

class Developer(db.Model):
    __tablename__ = 'Developer'

    DeveloperID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Website = db.Column(db.String)
    ContactInfo = db.Column(db.String)

    games = db.relationship("Game", back_populates="developer")
