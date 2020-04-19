import os
import random
from env import load_env
from pkg.tweepyHandler import TweepyHandler

# init & auth
load_env()
th = TweepyHandler(
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
)

# search
th.search_add_to_tweets(query="#myFirstTweet", result_type="recent", count=20)
th.search_add_to_tweets(query="#100DaysOfCode", result_type="recent", count=40)

# like
for seached_tweet in th.tweets:
    th.do_like_to_tweet(seached_tweet)
