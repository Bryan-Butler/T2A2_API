from main import ma
from marshmallow import fields, Schema

class DeveloperSchema(Schema):
    DeveloperID = fields.Integer(dump_only=True) 
    Name = fields.String(required=True)
    Website = fields.String()
    ContactInfo = fields.String()