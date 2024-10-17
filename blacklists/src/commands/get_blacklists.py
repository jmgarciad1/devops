from .base_command import BaseCommannd
from ..models.blacklist import Blacklist, BlacklistSchema
from ..session import Session

class GetBlacklists(BaseCommannd):
    def __init__(self, data):
        self.data = data

    def execute(self):
        session = Session()
        blacklists = session.query(Blacklist).all()

        blacklists = BlacklistSchema(many=True).dump(blacklists)
        session.close()

        return blacklists
