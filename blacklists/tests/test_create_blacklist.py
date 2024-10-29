from blacklists.src.commands.create_blacklist import CreateBlacklist
from blacklists.src.commands.get_blacklist import GetBlacklist

import uuid
import blacklists.tests.funtions as f

class TestCreateBlacklist():

    def create_blacklist(self):
        str_uuid = str(uuid.uuid4())

        data = {
            'id': str_uuid,
            'email': 'email_test_' + str_uuid + '@gmail.com',
            'app_uuid': str_uuid,
            'blocked_reason': 'blocked_reason_test',
            'ip': '127.0.0.1',
            'createdAt': '2024-10-29 00:00:00',
        }

        blacklist = f.save_line_file('blacklists/tests/blacklist.csv', data)

        return blacklist
