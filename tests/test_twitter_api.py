import os
import sys
import unittest
from birdy.twitter import UserClient


class TestTwitterAPI(unittest.TestCase):
    """
    This module is used to test Twitter API with the given configurations.
    """

    username = 'TheGeekyWay'
    
    def test_api_call(self):
        keys = tweetme.manage_token()
        if not tweetme.manage_token():
            print(("Twitter API cannot be tested if config.json is "
                                "not present with valid Token/Keys."))
        else:
            client = UserClient(*keys)
            self.assertTrue(client.api.users.show.get(screen_name=self.username).data["screen_name"], self.username)


'''
Since tweetme.py is now present in parent directory we need to add appropriate path in order to
access it as a module.
Path is added with respect to the location user is running the tests from.
'''
parent_directory_path = os.getcwd().split('/')
if 'tests' in parent_directory_path:
    parent_directory_path = parent_directory_path[:len(os.getcwd().split('/'))-1]
parent_directory_path = '/'.join(parent_directory_path)
if parent_directory_path not in sys.path:
    sys.path.append(parent_directory_path)

import tweetme

unittest.main()
