from marshmallow import Schema, fields

class UserLibrarySchema(Schema):
    UserLibrary_ID = fields.Integer(dump_only=True)  
    User_ID = fields.Integer()
    Game_ID = fields.Integer()
    Purchase_Date = fields.DateTime()
    Playtime = fields.Integer()
    Status = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")