from marshmallow import fields, validate

from main.schemas.base import BaseSchema


class AuthorSchema(BaseSchema):
    author_id = fields.Integer(require=True)


class ItemCreateSchema(BaseSchema):
    name = fields.String(validate=validate.Length(min=1, max=255), require=True)
    description = fields.String(validate=validate.Length(min=1, max=1024), require=True)
    author_id = fields.Integer(require=True)
    category_id = fields.Integer(require=True)


class ItemUpdateCategorySchema(BaseSchema):
    item_id = fields.Integer(require=True)
    author_id = fields.Integer(require=True)
    category_id = fields.Integer(require=True)


class ItemUpdateDescriptionSchema(BaseSchema):
    item_id = fields.Integer(require=True)
    description = fields.String(validate=validate.Length(min=1, max=1024), require=True)
    author_id = fields.Integer(require=True)


class ItemDeleteSchema(BaseSchema):
    item_id = fields.Integer(require=True)
    author_id = fields.Integer(require=True)
    category_id = fields.Integer(require=True)


class ItemInfoSchema(BaseSchema):
    item_id = fields.Integer()
    name = fields.String()
    description = fields.String()
    author_id = fields.Integer()
    category_id = fields.Integer()
    created_time = fields.DateTime()
    updated_time = fields.DateTime()
