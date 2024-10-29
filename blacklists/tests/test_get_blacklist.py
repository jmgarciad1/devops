from blacklists.src.commands.get_blacklist import GetBlacklist

class TestGetBlacklist():

    def get_blacklist_not_exist_email(self):
        blacklist = GetBlacklist('email_xxx@gmail.com').execute()

        return blacklist

    def get_blacklist_exist_email(self):
        blacklist = GetBlacklist('email_test@gmail.com').execute()

        return blacklist
