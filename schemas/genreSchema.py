from marshmallow import Schema, fields

class GenreSchema(Schema):
    GenreID = fields.Integer(dump_only=True)  
    GenreName = fields.String(required=True)