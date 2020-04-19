import tweepy

class TweepyHandler:
    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.api = None
        self.me = None
        self.follower_ids = []
        self.tweets = []
        self.__auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def __auth(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit = True)
        self.api = api
        self.me = api.me()

    def search_add_to_tweets(self, query, count=30, result_type="recent"):
        search_results = self.api.search(
            q=query,
            result_type=result_type,
            tweet_mode='extended',
            count=count
        )
        tweet_array = []
        for tweet in search_results:
            if not "RT @" in tweet.full_text[0:4]:
                self.tweets.append(tweet)

    def get_follower_ids(self):
        self.follower_ids = self.api.followers_ids(self.me.screen_name)

    def get_follower_timeline(self, each_count=10):
        for u_id in self.followers_ids:
            tweets = self.api.user_timeline(user_id=u_id, count=each_count)
            for t in tweets:
                self.tweets.append(t)

    def do_like_to_tweet(self, tweet):
        if not tweet.favorited:
            self.api.create_favorite(tweet.id)

    def do_retweet_to_tweet(self, tweet):
        if not tweet.retweeted:
            self.api.retweet(tweet.id)

    def do_reply_to_tweet(self, tweet, text):
        self.api.update_status(
            status = text,
            in_reply_to_status_id = tweet.id,
            auto_populate_reply_metadata=True
        )

if __name__ == '__main__':
    pass
