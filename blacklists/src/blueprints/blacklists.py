from flask import Flask, jsonify, request, Blueprint
from ..commands.authenticate import Authenticate
from ..commands.create_blacklist import CreateBlacklist
from ..commands.get_blacklist import GetBlacklist
from ..errors.errors import TokenInvalid
blacklists_blueprint = Blueprint('blacklists', __name__)


@blacklists_blueprint.route('/blacklists', methods=['POST'])
def create():
    userId = Authenticate(request.headers).execute()

    if not userId:
        raise TokenInvalid()
    
    ip = request.remote_addr
    item = CreateBlacklist(request.get_json(), ip).execute()

    return jsonify(item), 201


@blacklists_blueprint.route('/blacklists/<email>', methods=['GET'])
def show(email):
    userId = Authenticate(request.headers).execute()

    if not userId:
        raise TokenInvalid()
    
    response = GetBlacklist(email).execute()

    return jsonify(response)
