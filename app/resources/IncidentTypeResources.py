from uuid import uuid4

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.IncidentTypeSchema import IncidentTypeSchema

from models.IncidentTypeModel import IncidentTypeModel

from core.utils import get_current_time

from core.database import db
from sqlalchemy.exc import SQLAlchemyError


blp = Blueprint("IncidentType", __name__, description="Operations on IncidentTypes")


@blp.route("/incident_types")
class IncidentTypesResource(MethodView):

    @blp.response(200, IncidentTypeSchema(many=True))
    def get(self):
        incident = IncidentTypeModel.query.all()
        return incident
    
    @blp.arguments(IncidentTypeSchema)
    @blp.response(201, IncidentTypeSchema)
    def post(self, incident_data):
        
        incident_data = {
            "id": str(uuid4()),
            **incident_data,
            "is_active": True,
            "created_at": get_current_time()
        }

        incident = IncidentTypeModel(**incident_data)
        
        try:
            db.session.add(incident)
            db.session.commit()
        except SQLAlchemyError as e:
            print(str(e))
            abort(500, message="Um erro ocorreu ao tentar salvar o incidente!")

        return incident

@blp.route("/incident_type/<string:incident_id>")
class IncidentTypeResource(MethodView):

    @blp.response(200, IncidentTypeSchema)
    def get(self, incident_id):
        incident = IncidentTypeModel.query.get_or_404(incident_id)
        return incident
    
    @blp.arguments(IncidentTypeSchema)
    @blp.response(204, IncidentTypeSchema)
    def patch(self, incident_data, incident_id):
        incident = IncidentTypeModel.query.get_or_404(incident_id)
        if incident:
            incident.name = incident_data.get('name')
            incident.is_active = incident_data.get('is_active') if incident_data.get('is_active') != None else True

        db.session.add(incident)
        db.session.commit()

    @blp.response(204, IncidentTypeSchema)
    def delete(self, incident_id):
        incident = IncidentTypeModel.query.get_or_404(incident_id)
        db.session.delete(incident)
        db.session.commit()