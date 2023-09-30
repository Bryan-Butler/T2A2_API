from main import db

class Developer(db.Model):
    __tablename__ = 'developer'

    developer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    website = db.Column(db.String)
    contact_info = db.Column(db.String)

    games = db.relationship("game", back_populates="developer")