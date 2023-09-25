from marshmallow import Schema, fields

class ReviewSchema(Schema):
    Review_ID = fields.Integer(dump_only=True) 
    User_ID = fields.Integer()
    Game_ID = fields.Integer()
    Rating = fields.Integer()
    Review_Description = fields.String()
    Review_Date = fields.DateTime()

   
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")

