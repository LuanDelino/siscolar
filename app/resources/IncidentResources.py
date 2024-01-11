from uuid import uuid4

import flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("Incident", __name__, description="Operations on incidents")

@blp.route("/incident")
class IncidentResource(MethodView):
    def get(self):
        return {"msg": "Teste incidente"}
    
    def post(self):
        abort()