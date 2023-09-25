from main import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    email = fields.Email(
        required=True,
        validate=validate.Length(min=5, max=15, error="Hey that's not an email!")
    )

    class Meta:
        fields = ("UserID", "Username", "Email", "RegistrationDate")