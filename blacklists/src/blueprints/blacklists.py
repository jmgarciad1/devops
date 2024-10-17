from flask import Flask, jsonify, request, Blueprint
from ..commands.create_blacklist import CreateBlacklist
from ..commands.get_blacklist import GetBlacklist
from ..commands.get_blacklists import GetBlacklists
from ..commands.delete_blacklist import DeleteBlacklist
from ..commands.reset import Reset

blacklists_blueprint = Blueprint('blacklists', __name__)


@blacklists_blueprint.route('/blacklists', methods=['POST'])
def create():
    ip = request.remote_addr
    item = CreateBlacklist(request.get_json(), ip).execute()
    return jsonify(item), 201


@blacklists_blueprint.route('/blacklists', methods=['GET'])
def index():
    blacklists = GetBlacklists(request.get_json()).execute()
    return jsonify(blacklists)


@blacklists_blueprint.route('/blacklists/<email>', methods=['GET'])
def show(email):
    response = GetBlacklist(email).execute()
    return jsonify(response)


@blacklists_blueprint.route('/blacklists/<id>', methods=['DELETE'])
def destroy(id):
    response = DeleteBlacklist(id).execute()
    return jsonify(response)


@blacklists_blueprint.route('/blacklists/ping', methods=['GET'])
def ping():
    return 'pong'


@blacklists_blueprint.route('/blacklists/reset', methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({'status': 'OK'})
