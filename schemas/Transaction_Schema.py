from marshmallow import Schema, fields

class TransactionSchema(Schema):
    Transaction_ID = fields.Integer(dump_only=True)  
    User_ID = fields.Integer()
    Game_ID = fields.Integer()
    Purchase_Date = fields.DateTime()
    Transaction_Amount = fields.Integer()
    Payment_Method = fields.String()
    Transaction_Status = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")