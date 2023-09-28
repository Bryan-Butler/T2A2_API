from marshmallow import Schema, fields

class GenreSchema(Schema):
    genre_id = fields.Integer(dump_only=True)  
    genre_name = fields.String(required=True)