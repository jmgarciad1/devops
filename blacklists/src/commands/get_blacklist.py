from commands.base_command import BaseCommannd
from models.blacklist import Blacklist
from session import Session
from errors.errors import InvalidParams

class GetBlacklist(BaseCommannd):
    def __init__(self, email):
        if email != None:
            self.email = email
        else:
            raise InvalidParams()

    def execute(self):
        session = Session()

        item = session.query(Blacklist).filter_by(email=self.email).all()

        session.close()

        if len(item) <= 0:
            return {'exist': False}
        else:
            return {'exist': True, 'blocked_reason': item[0].blocked_reason}
