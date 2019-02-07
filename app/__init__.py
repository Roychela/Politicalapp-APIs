from flask import Flask
from app.V1.routes.offices import bluprint as officesblueprint

def politicoapp():
    app = Flask(__name__)
    app.register_blueprint(officesblueprint)
    return app