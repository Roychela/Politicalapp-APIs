from flask import Flask
from app.V1.views.officeview import bluprint as officesblueprint
from app.V1.views.partyview import bluprint as partiesblueprint

def politicoapp():
    app = Flask(__name__)
    app.register_blueprint(officesblueprint)
    app.register_blueprint(partiesblueprint)
    return app