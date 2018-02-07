import os
import json
import unittest
import tweetme
from birdy.twitter import UserClient


class TestConfigFile(unittest.TestCase):
    """
    This test module will run only to test manage_token() method.
    """

    def test_1_nofile(self):
        """
        Test the module when no config.json is present in the project directory.
        """

        self.assertFalse(tweetme.manage_token('testconfig.json'))

    
    def test_2_initialfile(self):
        """
        Test the module when config.json is present in the project directory.
        In this case, config.json contains atlest 1 Token/Key as 0.
        """

        self.assertFalse(tweetme.manage_token('testconfig.json'))

    
    def test_3_sampleconfig(self):
        """
        Test the module with sample configuration on Token/Key inside config.json
        ie. other than 0 as Token/Key for all the requirements.
        """

        with open('testconfig.json', mode='w') as f:
            json.dump({ 'consumer_key': 1, 
                        'consumer_secret': 1,
                        'access_token': 1,
                        'access_token_secret': 1,
                        }, f)
        self.assertTrue(tweetme.manage_token('testconfig.json'))

    
    def test_4_removing_config(self):
        """
        This test only removes config.json created and used by above tests.
        """

        try:
            os.remove("testconfig.json")
            self.assertTrue(True)
        except:
            self.assertTrue(False)


@unittest.skipIf(not tweetme.manage_token(), ("Twitter API cannot be tested if config.json is "
                             "not present with valid Token/Keys."))
class TestTwitterAPI(unittest.TestCase):
    """
    This module is used to test Twitter API with the given configurations.
    """

    username = 'TheGeekyWay'
    keys = tweetme.manage_token()

    def test_1_api_call(self):
        client = UserClient(*self.keys)
        self.assertTrue(client.api.users.show.get(screen_name=self.username).data["screen_name"], self.username)


class TestGettingTweets(unittest.TestCase):
    """
    Test the function get_tweet for Tweets file
    """
    def test_1_without_tweets_file(self):
        self.assertFalse(tweetme.get_tweet(tweets_file='temptweets.txt', turn_file='tempturn.txt'))

    def test_2_removing_temp_files(self):
        try:
            os.remove("temptweets.txt")
            os.remove("tempturn.txt")
            self.assertTrue(True)
        except:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
