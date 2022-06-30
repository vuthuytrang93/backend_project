from main.schemas.base import BaseSchema
from marshmallow import EXCLUDE, fields, validate, ValidationError


class ItemInSchema(BaseSchema):
    name = fields.Str(validate=validate.Length(min=1, max=255), require=True)
    description = fields.Str(validate=validate.Length(min=1, max=1024), require=True)
    author_id = fields.Int(require=True)
    category_id = fields.Int(require=True)


class ItemOutSchema(BaseSchema):
    name = fields.Str(validate=validate.Length(min=1, max=255), require=True)
    description = fields.Str(validate=validate.Length(min=1, max=1024), require=True)
    author_id = fields.Int(require=True)
    category_id = fields.Int(require=True)
    created_time = fields.DateTime()
    updated_time = fields.DateTime()


