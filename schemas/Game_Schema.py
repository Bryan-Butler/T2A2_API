from marshmallow import Schema, fields

class GameSchema(Schema):
    Game_ID = fields.Integer(dump_only=True)
    Genre_ID = fields.Integer()
    Developer_ID = fields.Integer()
    Publisher_ID = fields.Integer()
    Title = fields.String(required=True)
    Release_Date = fields.DateTime()
    Avg_User_Rating = fields.Float()
    Num_User_Rating = fields.Integer()

   
    genre = fields.Nested("GenreSchema")
    developer = fields.Nested("DeveloperSchema")
    publisher = fields.Nested("PublisherSchema")
    user_library = fields.Nested("UserLibrarySchema", many=True)
    transactions = fields.Nested("TransactionSchema", many=True)
    reviews = fields.Nested("ReviewSchema", many=True)