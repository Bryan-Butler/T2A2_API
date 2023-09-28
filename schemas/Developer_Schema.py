from main import ma
from marshmallow import fields, Schema

class DeveloperSchema(Schema):
    developer_id = fields.Integer(dump_only=True) 
    name = fields.String(required=True)
    website = fields.String()
    contact_info = fields.String()