# tweet-me
A bot to tweet articles from www.TheGeekyWay.com

### Pre-requisites

- `git clone https://github.com/TheGeekyWay/tweet-me.git`
- `cd tweet-me`
- `pip install pipenv`
- `pipenv install`

### Important files

- Create a file named `tweets.txt` whose each line should be in below format

`What are dotfiles? :: http://thegeekyway.com/what-are-dotfiles/`
`[Ultimate Guide] How SSH works? :: http://thegeekyway.com/ultimate-guide-how-ssh-works/`

- As you can see, each line has two parts separated by `::`. It's upto you what the content should be for each part.

### The First Run

- Run the command `pipenv run python tweetme.py`. You'll get a message asking you to add Twitter API configuration inside `config.json`. Use [Twitter Application Management](https://apps.twitter.com) and create a new application.

### Ready, Set, Go

- Run the command `pipenv run python tweetme.py` now and bot will start posting tweets from `tweets.txt`.
- You might get result similar to `You tweet is out in the world. Check it out https://twitter.com/TheGeekyWay/status/961375179879342080`
- Everytime you run above command one tweet below the previous one will be posted.

### Hello Hello Testing

- tweet-me supports unit testing with the help of `unittest` module by python.
- There are 3 type of test you can perform.
    1) Testing for configuration file by running `pipenv run python tests/test_config.py`
    2) Testing for tweets file by running `pipenv run python tests/test_getting_tweets.py`
    3) Testing for Twitter API by running `pipenv run python tests/test_twitter_api.py`
- To understand what is being tested feel free to open above files as it has been self documented.

### How everything works

- The entire process is divided into 3 parts.
    1) Checking the Configuration file (`config.json`)
    2) Checking the Tweets file (`tweets.txt`)
    3) Creating a Twitter object using the configuration and sending tweet over it.

- Look into the `tweetme.py` and read through the functions (also self documented) in order to find more details how everything works.

### Contributors

- [Shashank Kumar](https://blog.shankyxyz) (@realslimshanky)
