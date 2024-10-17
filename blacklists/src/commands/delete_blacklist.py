from .base_command import BaseCommannd
from ..models.blacklist import Blacklist
from ..session import Session
from ..errors.errors import InvalidParams, NotFoundError


class DeleteBlacklist(BaseCommannd):
    def __init__(self, item_id):
        if self.is_uuid(item_id):
            self.item_id = item_id
        else:
            raise InvalidParams()

    def execute(self):
        session = Session()
        if len(session.query(Blacklist).filter_by(id=self.item_id).all()) <= 0:
            session.close()
            raise NotFoundError()

        item = session.query(Blacklist).filter_by(id=self.item_id).one()
        session.delete(item)
        session.commit()
        session.close()

        return {'message': 'Item deleted'}
