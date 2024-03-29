from flask import Blueprint, jsonify, request

{routes_name}_blueprint = Blueprint(f'{routes_name}', __name__)


@{routes_name}_blueprint.route(f'/{routes_name}', methods=['GET'])
def get_{routes_name}():
    return jsonify([f'{routes_name} 1', f'{routes_name} 2'])


@{routes_name}_blueprint.route(f'/{routes_name}', methods=['POST'])
def post_{routes_name}():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@{routes_name}_blueprint.route(f'/{routes_name}/<{routes_name}_id>', methods=['PATCH'])
def patch_{routes_name}({routes_name}_id):
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    return jsonify(data)


@{routes_name}_blueprint.route(f'/{routes_name}/<{routes_name}_id>', methods=['DELETE'])
def delete_{routes_name}({routes_name}_id):
    return '', 204
