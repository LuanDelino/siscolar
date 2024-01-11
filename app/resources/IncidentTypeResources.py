from uuid import uuid4

import flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("IncidentType", __name__, description="Operations on IncidentTypes")

@blp.route("/incidentype")
class IncidentTypeResource(MethodView):
    def get(self):
        return {"msg": "Teste IncidentType"}
    
    def post(self):
        abort()