from marshmallow import Schema, fields

class GenreSchema(Schema):
    Genre_ID = fields.Integer(dump_only=True)  
    Genre_Name = fields.String(required=True)