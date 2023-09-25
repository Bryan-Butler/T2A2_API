from marshmallow import Schema, fields

class PublisherSchema(Schema):
    PublisherID = fields.Integer(dump_only=True)  
    Name = fields.String(required=True)
    Website = fields.String()
    Contactinfo = fields.String()

    
    games = fields.Nested("GameSchema", many=True, exclude=("publisher",))
