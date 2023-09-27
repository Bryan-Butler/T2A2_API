from main import db
from sqlalchemy import DateTime

class Transactions():
    __tablename__ = 'transactions'

    Transaction_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, db.ForeignKey('User.User_ID'))
    Game_ID = db.Column(db.Integer, db.ForeignKey('Game.Game_ID'))
    Purchase_Date = db.Column(DateTime)
    Transaction_Amount = db.Column(db.Integer)
    Payment_Method = db.Column(db.String)
    Transaction_Status = db.Column(db.String)

    # Define many-to-one relationships
    user = db.relationship("User", back_populates="transactions")
    game = db.relationship("Game", back_populates="transactions")

    #purchase date datetime
    #purchase_at
    #what is the purchase amount saved as, always the lowest so cents