from marshmallow import EXCLUDE, ValidationError, fields, validate

from main.schemas.base import BaseSchema


class UserLogInSchema(BaseSchema):
    email = fields.Email(validate=validate.Length(min=1, max=255), require=True)
    password = fields.String(validate=validate.Length(min=1, max=255), require=True)


class UserCreateSchema(BaseSchema):
    name = fields.String(validate=validate.Length(min=1, max=255), require=True)
    email = fields.Email(validate=validate.Length(min=1, max=255), require=True)
    password = fields.String(validate=validate.Length(min=6, max=255), require=True)


class UserInfoSchema(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    email = fields.Email()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()
