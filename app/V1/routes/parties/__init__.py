from flask import jsonify, make_response, request
from app.V1.routes import bluprint
from app.V1.models import PoliticalPartiesModel


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
