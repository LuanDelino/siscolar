from uuid import uuid4

import flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("Grade", __name__, description="Operations on Grades")

@blp.route("/grade")
class GradeResource(MethodView):
    def get(self):
        return {"msg": "Teste Grade"}
    
    def post(self):
        abort()