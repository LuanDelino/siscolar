from uuid import uuid4
from core.database import db

class GradeModel(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid4())
    name = db.Column(db.String, nullable=False)