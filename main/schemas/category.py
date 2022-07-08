from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class AuthorSchema(BaseSchema):
    author_id = fields.Integer(require=True)


class AuthorCategorySchema(BaseSchema):
    name = fields.String(validate=validate.Length(min=1, max=255), require=True)
    author_id = fields.Integer(require=True)


class AuthorCategoryIdSchema(BaseSchema):
    category_id = fields.Integer(require=True)
    author_id = fields.Integer(require=True)


class CategoryInfoSchema(BaseSchema):
    id = fields.Integer()
    name = fields.String()
    author_id = fields.Integer()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()

