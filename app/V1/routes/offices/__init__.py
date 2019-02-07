from flask import jsonify, make_response, request
from app.V1.routes import bluprint
from app.V1.models import PoliticalOfficeModel


@bluprint.route("/offices", methods= ["GET"] )
def get_all_offices():
    return make_response(jsonify({
        "status": 200,
        "data": PoliticalOfficeModel.view_all_offices() }), 200)