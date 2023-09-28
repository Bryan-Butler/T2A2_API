from main import db
from sqlalchemy import DateTime

class Transactions():
    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.game_id'))
    purchase_date = db.Column(DateTime)
    transaction_amount = db.Column(db.Integer)
    payment_method = db.Column(db.String)
    transaction_status = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="transactions")
    game = db.relationship("Game", back_populates="transactions")

    #purchase date datetime
    #purchase_at
    #what is the purchase amount saved as, always the lowest so cents