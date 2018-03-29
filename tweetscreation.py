from feedparser import parse
from sys import argv

tweets_file = "tweets.txt"

def feed_generation(url):
    feed = parse(url)
    if not feed["items"]:
        print("Feed url incorrect")
    else:
        with open(tweets_file, mode='w') as f:
            for x in feed["items"]:
                f.write('{} :: {}\n'.format(x["title"], x["link"]))
        print("{} has been successfully created with latest feeds.".format(tweets_file))


if len(argv) < 2:
    print("Please enter a feed url after 'python tweetscreation.py'")
else:
    feed_generation(argv[1])
