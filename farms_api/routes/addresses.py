from flask import Blueprint, jsonify, request

addresses_blueprint = Blueprint('addresses', __name__)


@addresses_blueprint.route('/addresses', methods=['GET'])
def get_addresses():
    return jsonify(['address 1', 'address 2'])


@addresses_blueprint.route('/addresses', methods=['POST'])
def post_addresses():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@addresses_blueprint.route('/addresses/<address_id>', methods=['PATCH'])
def patch_addresses(address_id):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@addresses_blueprint.route('/addresses/<address_id>', methods=['DELETE'])
def delete_addresses(address_id):
    return '', 204
