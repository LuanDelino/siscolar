from uuid import uuid4

import flask
from flask.views import MethodView
from flask_smorest import Blueprint, abort


blp = Blueprint("Students", __name__, description="Operations on Students")

@blp.route("/students")
class StudentsResource(MethodView):
    def get(self):
        return {"msg": "Teste Students"}
    
    def post(self):
        abort()