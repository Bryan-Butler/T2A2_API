from marshmallow import Schema, fields

class ReviewSchema(Schema):
    review_id = fields.Integer(dump_only=True) 
    user_id = fields.Integer()
    game_id = fields.Integer()
    rating = fields.Integer()
    review_description = fields.String()
    revie_date = fields.DateTime()

   
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")

