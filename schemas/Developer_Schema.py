from main import ma
from marshmallow import fields, Schema

class DeveloperSchema(Schema):
    Developer_ID = fields.Integer(dump_only=True) 
    Name = fields.String(required=True)
    Website = fields.String()
    Contact_Info = fields.String()