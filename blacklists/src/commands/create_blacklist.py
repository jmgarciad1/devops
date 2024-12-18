from commands.base_command import BaseCommannd
from models.blacklist import Blacklist, BlacklistSchema
from session import Session
from errors.errors import IncompleteParams, EmailExist

class CreateBlacklist(BaseCommannd):
    def __init__(self, data, ip=None):
        self.data = data
        self.email = data['email']
        if ip != None:
            self.data['ip'] = ip

    def execute(self):
        try:

            session = Session()
            item = session.query(Blacklist).filter_by(email=self.email).all()

            if len(item) > 0:
                raise EmailExist()

            load_data = BlacklistSchema(
                only=('email', 'app_uuid', 'blocked_reason', 'ip')
            ).load(self.data)
            
            blacklist = Blacklist(**load_data)

            session = Session()
            session.add(blacklist)
            session.commit()
            session.close()

            return {'message': 'Item created'}
        except TypeError:
            raise IncompleteParams
