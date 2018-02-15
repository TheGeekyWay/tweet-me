import os
import json
import twitter
import logging
from birdy.twitter import UserClient

logging.basicConfig(filename='tweetme.log', format='%(asctime)s %(message)s', level=logging.DEBUG)

def get_config_from_file(filename="config.json"):
    """
    This function will check for the config.json file which holds the Twitter API
    Tokens and Keys and will also give a user friendly message if they are
    invalid. New file is created if not present in the project directory.

    Returns False: if config.json is missing of has invalid configuration
    Returns tuple (containing configurations): if config.json is present with
                                                valid configuration
    """

    if filename not in os.listdir():
        with open(filename, mode='w') as f:
            json.dump({ 'consumer_key': 0, 
                        'consumer_secret': 0,
                        'access_token': 0,
                        'access_token_secret': 0,
                        }, f)
            return False
    else:
        with open(filename, mode='r') as f:
            config = json.loads(f.read())
            if 0 not in config.values():
                return (config["consumer_key"],
                        config["consumer_secret"],
                        config["access_token"],
                        config["access_token_secret"],
                )
            else:
                return False


def get_next_tweet_from_file(tweets_file='tweets.txt', turn_file='next_tweet_index.txt'):
    """
    This function reads Tweets file and Turn file and gets the next tweet.

    Returns False: if tweets.txt is not present
    Returns next Tweet: if valid tweets.txt is present
    """

    if tweets_file not in os.listdir():
        """When tweets.txt is not present"""
        with open(tweets_file, mode='w') as f:
            f.write('Tweet :: URL\n')
        with open(turn_file, mode='w') as f:
            f.write('0')
        return False
    
    elif turn_file not in os.listdir():
        """When next_tweet_index.txt is not present, creates a new next_tweet_index.txt and writes 1 in it
        and return the first tweet from tweets.txt"""
        with open(turn_file, mode='w') as f:
            f.write('1')
        with open(tweets_file, mode='r') as f:
            tweet_text =  f.readline()
        return tweet_text.split("::")
    else:
        """When both files are present, check next_tweet_index.txt and use it's value as index to
        find the next tweet from tweets.txt and write index + 1 in next_tweet_index.txt"""
        with open(turn_file, mode='r') as f:
            turn = int(f.readline())
        with open(tweets_file, mode='r') as f:
            tweets = f.readlines()
            if len(tweets) <= turn:
                turn = 0
            with open(turn_file, mode='w') as f:
                f.write(str(turn + 1))
        return tweets[turn].split("::")


def manage_twitter_client():
    """
    This function will create twitter client using configurations and send tweet.
    """

    configError = ("Please open config.json file located in the project "
        "directory and replace the value '0' of all the tokens and keys in "
        "order to make this bot work. Visit https://apps.twitter.com/ in "
        "order to get your tokens and keys.")

    keys = get_config_from_file()
    if not keys:
        logging.error(configError)
    else:
        tweet = get_next_tweet_from_file()
        if tweet:
            client = UserClient(*keys)
            response = client.api.statuses.update.post(status='{} {}'.format(tweet[0], tweet[1]))
            logging.info(('You tweet is out in the world.'
                          'Check it out https://twitter.com/{}/status/{}').format(
                                                            response.data["user"]["screen_name"],
                                                            response.data["id_str"]))


if __name__ == '__main__':
    manage_twitter_client()
