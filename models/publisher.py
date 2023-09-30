from main import db

class Publisher(db.Model):
    __tablename__ = 'publisher'

    publisher_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)
    contact_info = db.Column(db.String)

    games = db.relationship("Game", back_populates="publisher")