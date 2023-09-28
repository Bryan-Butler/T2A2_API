from marshmallow import Schema, fields

class UserLibrarySchema(Schema):
    user_library_id = fields.Integer(dump_only=True)  
    user_id = fields.Integer()
    game_id = fields.Integer()
    purchase_date = fields.DateTime()
    play_time = fields.Integer()
    status = fields.String()

    
    user = fields.Nested("UserSchema")
    game = fields.Nested("GameSchema")