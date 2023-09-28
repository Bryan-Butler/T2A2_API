from marshmallow import Schema, fields

class PublisherSchema(Schema):
    publisher_id = fields.Integer(dump_only=True)  
    name = fields.String(required=True)
    website = fields.String()
    contact_info = fields.String()

    
    games = fields.Nested("GameSchema", many=True, exclude=("publisher",))
