from flask import jsonify, make_response, request
from app.V1.views import bluprint
from app.V1.models import PoliticalOfficeModel


@bluprint.route("/offices", methods= ["GET"] )
def get_all_offices():
    return make_response(jsonify({
        "status": 200,
        "data": PoliticalOfficeModel.view_all_offices() }), 200)

@bluprint.route("/offices", methods= ["POST"])
def create_office():
    data = request.get_json()
    try:
        name = data['name']
        id = data['id']
        type = data['type']
    except:
        return make_response(jsonify({
            "status": 400,
            "error": "All fields must be filled"
        }), 400)
    newoffice = PoliticalOfficeModel(name=name, type=type, id=id)
    newoffice.saveoffice()

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "id": id,
            "name": name,
            "type": type
            }]
    }), 201)        


@bluprint.route("/offices/<int:office_id>", methods=["GET"])
def get_single_office(office_id):

    office = PoliticalOfficeModel.get_specific_office(office_id)

    if office:
        return make_response(jsonify({
            "status": 200,
            "data": office
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Office not found on server"
    }), 404)    