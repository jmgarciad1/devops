from .base_command import BaseCommannd
from ..models.blacklist import Blacklist, BlacklistSchema
from ..session import Session
from ..errors.errors import IncompleteParams

class CreateBlacklist(BaseCommannd):
    def __init__(self, data, ip=None):
        self.data = data
        if ip != None:
            self.data['ip'] = ip

    def execute(self):
        try:

            load_data = BlacklistSchema(
                only=('email', 'app_uuid', 'blocked_reason')
            ).load(self.data)
            
            blacklist = Blacklist(**load_data)

            session = Session()
            session.add(blacklist)
            session.commit()
            session.close()

            return {'message': 'Item created'}
        except TypeError:
            raise IncompleteParams
