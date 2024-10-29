from blacklists.tests.test_create_blacklist import TestCreateBlacklist
from blacklists.tests.test_get_blacklist import TestGetBlacklist

import unittest

class TestBlacklist(unittest.TestCase):    

    def test_create_blacklist_not_exist_email(self):
        blacklist = TestCreateBlacklist().create_blacklist_not_exist_email()

        self.assertEqual(blacklist['message'], 'Item created')

    def test_create_blacklist_exist_email(self):
        blacklist = TestCreateBlacklist().create_blacklist_exist_email()

        self.assertEqual(blacklist['exist'], True)

    def test_get_blacklist_not_exist_email(self):
        blacklist = TestGetBlacklist().get_blacklist_not_exist_email()

        self.assertEqual(blacklist['exist'], False)

    def test_get_blacklist_exist_email(self):
        blacklist = TestGetBlacklist().get_blacklist_exist_email()

        self.assertEqual(blacklist['exist'], True)

if __name__ == '__main__':
    unittest.main()