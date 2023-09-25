from main import db
from sqlalchemy import DateTime

class Transactions():
    __tablename__ = 'Transactions'

    TransactionID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.UserID'))
    GameID = db.Column(db.Integer, db.ForeignKey('Game.GameID'))
    PurchaseDate = db.Column(DateTime)
    TransactionAmount = db.Column(db.Integer)
    PaymentMethod = db.Column(db.String)
    TransactionStatus = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="transactions")
    game = db.relationship("Game", back_populates="transactions")

    #purchase date datetime
    #purchase_at
    #what is the purchase amount saved as, always the lowest so cents