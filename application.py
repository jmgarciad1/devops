from blacklists.src.errors.errors import ApiError
from blacklists.src.blueprints.blacklists import blacklists_blueprint
from blacklists.src.models.model import Base
from blacklists.src.session import Session, engine
from flask import Flask

app = Flask(__name__)
app.register_blueprint(blacklists_blueprint)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.debug = True
    app.run()
