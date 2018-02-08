import os
import sys
import unittest


class TestGettingTweets(unittest.TestCase):
    """
    Test the function get_tweet for Tweets file
    """

    
    def test_1_without_tweets_file(self):
        self.assertFalse(tweetme.get_tweet(tweets_file='temp_tweets.txt', turn_file='temp_next_tweet_index.txt'))

    def test_2_removing_temp_files(self):
        try:
            os.remove("temp_tweets.txt")
            os.remove("temp_next_tweet_index.txt")
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
