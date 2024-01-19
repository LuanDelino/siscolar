from uuid import uuid4

from marshmallow import Schema, fields


class GradeSchema(Schema):
    id: uuid4 = fields.UUID(dumps=True)
    name: str = fields.Str(required=True)