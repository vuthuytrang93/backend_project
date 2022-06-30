from main.schemas.base import BaseSchema
from marshmallow import EXCLUDE, fields, validate, ValidationError


class UserInSchema(BaseSchema):
    name = fields.String(validate=validate.Length(min=1, max=255), require=True)
    email = fields.Email(validate=validate.Length(min=1, max=255), require=True)
    hashed_password = fields.String(validate=validate.Length(min=1, max=255), require=True)


class UserOutSchema(BaseSchema):
    name = fields.String(validate=validate.Length(min=1, max=255), require=True)
    email = fields.Email(validate=validate.Length(min=1, max=255), require=True)
    created_time = fields.DateTime(require=True)
    updated_time = fields.DateTime(require=True)


