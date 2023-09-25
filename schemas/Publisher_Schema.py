from marshmallow import Schema, fields

class PublisherSchema(Schema):
    Publisher_ID = fields.Integer(dump_only=True)  
    Name = fields.String(required=True)
    Website = fields.String()
    Contact_Info = fields.String()

    
    games = fields.Nested("GameSchema", many=True, exclude=("publisher",))
