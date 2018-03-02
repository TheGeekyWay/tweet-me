import path
import unittest
from birdy.twitter import UserClient


class TestTwitterAPI(unittest.TestCase):
    """
    This module is used to test Twitter API with the given configurations.
    """

    username = 'TheGeekyWay'
    
    def test_api_call(self):
        keys = tweetme.get_config_from_file()
        if not tweetme.get_config_from_file():
            print(("Twitter API cannot be tested if config.json is "
                                "not present with valid Token/Keys."))
        else:
            client = UserClient(*keys)
            self.assertTrue(client.api.users.show.get(screen_name=self.username).data["screen_name"], self.username)


import tweetme

unittest.main()
