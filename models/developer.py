from main import db

class Developer(db.Model):
    __tablename__ = 'developers'

    Developer_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Website = db.Column(db.String)
    Contact_Info = db.Column(db.String)

    games = db.relationship("Game", back_populates="developer")
