from main import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    email = fields.Email(
        required=True,
        validate=[
            validate.Length(min=5, max=50, error="Email must be between 5 and 50 characters."),
            validate.Email(error="Invalid email format."),
        ]
    )

    username = fields.String(
        required=True,
        validate=validate.Length(min=3, max=20, error="Username must be between 3 and 20 characters.")
    )

    password = fields.String(
        required=True,
        validate=validate.Length(min=4, error="Password must be at least 4 characters long.")
    )


    class Meta:
        fields = ("user_id", "username", "email", "registration_date")