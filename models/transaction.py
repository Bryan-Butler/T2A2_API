from main import db
from sqlalchemy import DateTime

class Transactions(db.Model):
    __tablename__ = 'transaction'

    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    purchase_date = db.Column(DateTime)
    transaction_amount = db.Column(db.Integer)
    payment_method = db.Column(db.String)
    transaction_status = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="transactions")
    game = db.relationship("Game", back_populates="transactions")