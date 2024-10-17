from flask import Flask, jsonify, request, Blueprint
from ..commands.create_blacklist import CreateBlacklist
from ..commands.get_blacklist import GetBlacklist

blacklists_blueprint = Blueprint('blacklists', __name__)


@blacklists_blueprint.route('/blacklists', methods=['POST'])
def create():
    ip = request.remote_addr
    item = CreateBlacklist(request.get_json(), ip).execute()
    return jsonify(item), 201


@blacklists_blueprint.route('/blacklists/<email>', methods=['GET'])
def show(email):
    response = GetBlacklist(email).execute()
    return jsonify(response)
