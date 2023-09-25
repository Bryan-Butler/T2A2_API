from marshmallow import Schema, fields

class ReviewSchema(Schema):
    ReviewID = fields.Integer(dump_only=True) 
    UserID = fields.Integer()
    GameID = fields.Integer()
    Rating = fields.Integer()
    ReviewDescription = fields.String()
    ReviewDate = fields.DateTime()

   
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")

