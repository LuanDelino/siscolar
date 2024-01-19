from uuid import uuid4

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.GradeSchema import GradeSchema
from models.GradeModel import GradeModel

from core.database import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("Grades", __name__, description="Operations on grades")

@blp.route("/grades")
class IncidentResource(MethodView):

    @blp.response(200, GradeSchema(many=True))
    def get(self):
        grades = GradeModel.query.all()
        return grades
    
    @blp.arguments(GradeSchema)
    @blp.response(201, GradeSchema)
    def post(self, grade_data):

        grade_data = {
            "id": str(uuid4()),
            **grade_data
        }

        grade = GradeModel(**grade_data)
        try:
            db.session.add(grade)
            db.session.commit()
        except SQLAlchemyError as e:
            print(str(e))
            abort(500, message="Um erro ocorreu ao tentar salvar a serie!")

        return grade

@blp.route("/grade/<string:incident_id>")
class GradeResource(MethodView):
    @blp.response(200, GradeSchema)
    def get(self, incident_id):
        incident = GradeModel.query.get_or_404(incident_id)
        return incident
    
    @blp.arguments(GradeSchema)
    @blp.response(204, GradeSchema)
    def patch(self, incident_data, incident_id):
        incident = GradeModel.query.get_or_404(incident_id)
        if incident:
            incident.name = incident_data.get('name')
            
        db.session.add(incident)
        db.session.commit()

    @blp.response(204, GradeSchema)
    def delete(self, incident_id):
        incident = GradeModel.query.get_or_404(incident_id)
        db.session.delete(incident)
        db.session.commit()