from flask import Blueprint, jsonify, request

farmers_blueprint = Blueprint('farmers', __name__)


@farmers_blueprint.route('/farmers', methods=['GET'])
def get_farmers():
    return jsonify(['farmer 1', 'farmer 2'])


@farmers_blueprint.route('/farmers', methods=['POST'])
def post_farmers():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@farmers_blueprint.route('/farmers/<farmer_id>', methods=['PATCH'])
def patch_farmers(farmer_id):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@farmers_blueprint.route('/farmers/<farmer_id>', methods=['DELETE'])
def delete_farmers(farmer_id):
    return '', 204
