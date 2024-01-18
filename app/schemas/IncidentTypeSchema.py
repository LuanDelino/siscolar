from uuid import uuid4
from datetime import datetime

from marshmallow import Schema, fields


class IncidentTypeSchema(Schema):
    id: uuid4 = fields.UUID(dumps=True)
    name: str = fields.Str(required=True)
    is_active: bool = fields.Bool(dumps=True)
    created_at: datetime = fields.DateTime(dumps=True)