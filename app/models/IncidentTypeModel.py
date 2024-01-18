from uuid import uuid4
from core.database import db

class IncidentTypeModel(db.Model):
    __tablename__ = 'incident_type'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)