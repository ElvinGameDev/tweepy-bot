import os
from env import set_env

# set environ
from pkg.tweepyHandler import TweepyHandler
set_env()

# init & auth
th = TweepyHandler(
    os.environ["CONSUMER_KEY"],
    os.environ["CONSUMER_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_TOKEN_SECRET"]
)

# search & get tweets
th.search_add_to_tweets(query="#myFirstTweet", result_type="recent", count=20)
th.search_add_to_tweets(query="#100DaysOfCode", result_type="recent", count=40)

# action
for seached_tweet in th.tweets:
    try:
        th.do_like_to_tweet(seached_tweet)
    except Exception as e:
        print(e)
