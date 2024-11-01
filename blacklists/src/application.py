from errors.errors import ApiError
from blueprints.blacklists import blacklists_blueprint
from models.model import Base
from session import engine
from flask import Flask, jsonify

application = Flask(__name__)
application.register_blueprint(blacklists_blueprint)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(engine)

@application.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code

if __name__ == "__main__":
    application.run(host = "0.0.0.0",port = 5000, debug = True)
