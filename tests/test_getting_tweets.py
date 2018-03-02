import os
import path
import unittest


class TestGettingTweets(unittest.TestCase):
    """
    Test the function get_next_tweet_from_file for Tweets file

    Note: Naming after `test_` are important as they facilitate test to run in
          specific order as `unittest` runs test in alphabetical order of thier names.
    """

    
    def test_no_tweets_file(self):
        self.assertFalse(tweetme.get_next_tweet_from_file(tweets_file='temp_tweets.txt', turn_file='temp_next_tweet_index.txt'))

    def test_removing_temp_files(self):
        try:
            os.remove("temp_tweets.txt")
            os.remove("temp_next_tweet_index.txt")
            self.assertTrue(True)
        except:
            self.assertTrue(False)


import tweetme

unittest.main()
