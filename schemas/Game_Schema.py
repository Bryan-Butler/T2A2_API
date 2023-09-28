from marshmallow import Schema, fields

class GameSchema(Schema):
    game_id = fields.Integer(dump_only=True)
    genre_id = fields.Integer()
    developer_id = fields.Integer()
    publisher_id = fields.Integer()
    title = fields.String(required=True)
    release_date = fields.DateTime()
    avg_user_rating = fields.Float()
    num_user_rating = fields.Integer()

   
    genre = fields.Nested("GenreSchema")
    developer = fields.Nested("DeveloperSchema")
    publisher = fields.Nested("PublisherSchema")
    user_library = fields.Nested("UserLibrarySchema", many=True)
    transactions = fields.Nested("TransactionSchema", many=True)
    reviews = fields.Nested("ReviewSchema", many=True)