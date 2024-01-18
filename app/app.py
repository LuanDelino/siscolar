from flask import Flask
from flask_smorest import Api
from core.database import db
from models import IncidentTypeModel

from resources.IncidentResources import blp as IncidentBlueprint
from resources.GradeResource import blp as GradeBlueprint
from resources.IncidentTypeResources import blp as IncidentTypeBlueprint
from resources.StudentResource import blp as StudentBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "API de Ocorrencias Escolares"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@postgres:5432/siscolar"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

api.register_blueprint(IncidentTypeBlueprint)

db.init_app(app)

with app.app_context():
    db.create_all()
