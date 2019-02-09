from flask import jsonify, make_response, request
from app.V1.views import bluprint
from app.V1.models import PoliticalPartiesModel, allparties


@bluprint.route("/parties", methods= ["POST"])
def create_party():
    data = request.get_json()
    try:
        logoUrl = data['logoUrl']
        name = data['name']
        id = data['id']
        hqAddress = data['hqAddress']
    except:
        return make_response(jsonify({
            "status": 400,
            "error": "All fields must be filled"
        }), 400)
    newparty = PoliticalPartiesModel(name=name, hqAddress=hqAddress, id=id, logoUrl=logoUrl)
    newparty.saveparty()

    return make_response(jsonify({
        "status": 201,
        "data": [{
            "id": id,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }]
    }), 201)

@bluprint.route("/parties", methods= ["GET"] )
def get_all_parties():
    return make_response(jsonify({
        "status": 200,
        "data": PoliticalPartiesModel.view_all_parties() }), 200)


@bluprint.route("/parties/<int:party_id>", methods=["GET"])
def get_one_party(party_id):

    party = PoliticalPartiesModel.get_specific_party(party_id)

    if party:
        return make_response(jsonify({
            "status": 200,
            "data": party
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Party not found on server"
    }), 404)    

@bluprint.route("/parties/<int:party_id>", methods=["DELETE"])    
def delete_party(party_id):
    party = PoliticalPartiesModel.get_specific_party(party_id)
    allparties.remove(party[0])
    return make_response(jsonify({
        "status": 204,
        "data": [{"message": "Party successfully deleted"}]}), 204)
