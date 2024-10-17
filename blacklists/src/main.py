from .errors.errors import ApiError
from .blueprints.blacklists import blacklists_blueprint
from .models.model import Base
from .session import Session, engine
from flask import Flask, jsonify


app = Flask(__name__)
app.register_blueprint(blacklists_blueprint)

Base.metadata.create_all(engine)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code
