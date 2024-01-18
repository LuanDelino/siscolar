from uuid import uuid4

import flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("Grades", __name__, description="Operations on grades")

@blp.route("/grades")
class IncidentResource(MethodView):
    def get(self):
        return {"msg": "Teste incidente"}
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass