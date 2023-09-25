from marshmallow import Schema, fields

class UserLibrarySchema(Schema):
    UserLibraryID = fields.Integer(dump_only=True)  
    UserID = fields.Integer()
    GameID = fields.Integer()
    PurchaseDate = fields.DateTime()
    Playtime = fields.Integer()
    Status = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")