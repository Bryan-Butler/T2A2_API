from marshmallow import Schema, fields

class TransactionSchema(Schema):
    transaction_id = fields.Integer(dump_only=True)  
    user_id = fields.Integer()
    game_id = fields.Integer()
    purchase_date = fields.DateTime()
    transaction_amount = fields.Integer()
    payment_method = fields.String()
    transaction_status = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")