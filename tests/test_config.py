import os
import json
import path
import unittest


class TestConfigFile(unittest.TestCase):
    """
    This test module will run only to test manage_token() method.

    Note: Naming after `test_` are important as they facilitate test to run in
          specific order as `unittest` runs test in alphabetical order of thier names.
    """


    def test_config_file_not_present(self):
        """
        Case: When no config.json is present in the project directory.
        """

        self.assertFalse(tweetme.manage_token('testconfig.json'))

    
    def test_config_file_present(self):
        """
        Case: When config.json is present in the project directory.
        In this case, config.json contains atlest 1 Token/Key as 0.
        """

        self.assertFalse(tweetme.manage_token('testconfig.json'))

    
    def test_config_file_validation(self):
        """
        Case: With sample configuration on Token/Key inside config.json
        ie. other than 0 as Token/Key for all the requirements.
        """

        with open('testconfig.json', mode='w') as f:
            json.dump({ 'consumer_key': 1, 
                        'consumer_secret': 1,
                        'access_token': 1,
                        'access_token_secret': 1,
                        }, f)
        self.assertTrue(tweetme.manage_token('testconfig.json'))

    
    def test_removing_config(self):
        """
        Case: Only removes config.json created and used by above tests.
        """

        try:
            os.remove("testconfig.json")
            self.assertTrue(True)
        except:
            self.assertTrue(False)


import tweetme

unittest.main()
