from marshmallow import Schema, fields

class TransactionSchema(Schema):
    TransactionID = fields.Integer(dump_only=True)  
    UserID = fields.Integer()
    GameID = fields.Integer()
    PurchaseDate = fields.DateTime()
    TransactionAmount = fields.Integer()
    PaymentMethod = fields.String()
    TransactionStatus = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")