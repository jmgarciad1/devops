from blacklists.src.commands.create_blacklist import CreateBlacklist
from blacklists.src.commands.get_blacklist import GetBlacklist

import uuid

class TestCreateBlacklist():

    def create_blacklist_not_exist_email(self):
        str_uuid = str(uuid.uuid4())
        ip = '127.0.0.1'

        data = {
            'email': 'email_test_' + str_uuid + '@gmail.com',
            'app_uuid': str_uuid,
            'blocked_reason': 'blocked_reason_test'
        }

        blacklist = CreateBlacklist(data, ip).execute()

        return blacklist

    def create_blacklist_exist_email(self): 
        str_uuid = str(uuid.uuid4())
        ip = '127.0.0.1'

        data = {
            'email': 'email_test@gmail.com',
            'app_uuid': str_uuid,
            'blocked_reason': 'blocked_reason_test'
        }

        blacklist = GetBlacklist('email_test@gmail.com').execute()

        if blacklist['exist'] == False:
           blacklist = CreateBlacklist(data, ip).execute()
        
        blacklist = GetBlacklist('email_test@gmail.com').execute()

        return blacklist
