from marshmallow import Schema, fields

class GameSchema(Schema):
    GameID = fields.Integer(dump_only=True)
    GenreID = fields.Integer()
    DeveloperID = fields.Integer()
    PublisherID = fields.Integer()
    Title = fields.String(required=True)
    ReleaseDate = fields.DateTime()
    AvgUserRating = fields.Float()
    NumUserRating = fields.Integer()

   
    genre = fields.Nested("GenreSchema")
    developer = fields.Nested("DeveloperSchema")
    publisher = fields.Nested("PublisherSchema")
    user_library = fields.Nested("UserLibrarySchema", many=True)
    transactions = fields.Nested("TransactionSchema", many=True)
    reviews = fields.Nested("ReviewSchema", many=True)