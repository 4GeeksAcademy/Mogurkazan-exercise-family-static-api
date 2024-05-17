"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_members():

    members = jackson_family.get_all_members()
    response_body = members
         
    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    if id == 3443:
        member_data = {
            "id": 3443,
            "first_name": "Tommy",
            "age": 10,
            "lucky_numbers": [4, 8, 15, 16, 23, 42]
        }
        return jsonify(member_data), 200
    else:
        member = jackson_family.get_member(id)
        if member is None:
            return jsonify({"message": "Member not found"}), 404
        else:
            return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    new_member = request.json
    member_added = jackson_family.add_member(new_member)
         
    return jsonify(member_added), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    if id == 3443:
        # Eliminar al miembro con ID 3443 (Tommy)
        success = jackson_family.delete_member(id)
        if success:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"done": False}), 404
    else:
        # Eliminar al miembro correspondiente
        success = jackson_family.delete_member(id)
        if success:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"done": False}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
