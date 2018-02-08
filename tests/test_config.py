import os
import sys
import json
import unittest


class TestConfigFile(unittest.TestCase):
    """
    This test module will run only to test manage_token() method.

    Note: Numbers just after `test_` are important as they facilitate test to run in
          specific order as `unittest` runs test in alphabetical order of thier names.
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
