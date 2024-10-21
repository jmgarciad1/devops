from blacklists.src.errors.errors import ApiError
from blacklists.src.blueprints.blacklists import blacklists_blueprint
from blacklists.src.models.model import Base
from blacklists.src.session import Session, engine
from flask import Flask

application = Flask(__name__)
application.register_blueprint(blacklists_blueprint)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    application.run(port = 5000, debug = True)
