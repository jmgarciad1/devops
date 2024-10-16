from flask import Flask, jsonify, request, Blueprint
from ..commands.create_post import CreatePost
from ..commands.get_post import GetPost
from ..commands.get_posts import GetPosts
from ..commands.delete_post import DeletePost
from ..commands.reset import Reset

posts_blueprint = Blueprint('posts', __name__)


@posts_blueprint.route('/posts', methods=['POST'])
def create():
    userId = 'bf8792d2-3097-11ee-be56-0242ac120002'
    post = CreatePost(request.get_json(), userId).execute()
    return jsonify(post), 201


@posts_blueprint.route('/posts', methods=['GET'])
def index():
    userId = 'bf8792d2-3097-11ee-be56-0242ac120002'
    posts = GetPosts(request.args.to_dict(), userId).execute()
    return jsonify(posts)


@posts_blueprint.route('/posts/<id>', methods=['GET'])
def show(id):
    post = GetPost(id).execute()
    return jsonify(post)


@posts_blueprint.route('/posts/<id>', methods=['DELETE'])
def destroy(id):
    response = DeletePost(id).execute()
    return jsonify(response)


@posts_blueprint.route('/posts/ping', methods=['GET'])
def ping():
    return 'pong'


@posts_blueprint.route('/posts/reset', methods=['POST'])
def reset():
    Reset().execute()
    return jsonify({'status': 'OK'})
