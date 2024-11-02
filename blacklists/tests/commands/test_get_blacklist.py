import blacklists.tests.funtions as f

class TestGetBlacklist():

    def get_blacklist_exist_email(self, email):
        data = f.load_file('blacklists/tests/blacklist.csv')

        try:
            item = data[email]
            return {'exist': True, 'blocked_reason': item['blocked_reason']}            
        except KeyError:
            return {'exist': False}
