from main import ma
from marshmallow import fields, validate

class User_Schema(ma.Schema):
    email = fields.Email(
        required=True,
        validate=validate.Length(min=5, max=15, error="Hey that's not an email!")
    )

    class Meta:
        fields = ("User_ID", "Username", "Email", "Registration_Date")