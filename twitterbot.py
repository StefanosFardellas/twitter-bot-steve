import tweepy
import time

# Place your Twitter Keys here
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'	

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def like_and_retweet():
    print("Looking for tweets...")
    for tweet in tweepy.Cursor(api.search, q=('#HelloWorld OR #JavaScript OR #Python OR #Python3 OR #100DaysOfCode OR #C OR #MachineLearning OR #CodeNewbies OR #WebDevelopment OR #Coding OR #DeepLearning OR #TSLA OR #TESLA OR #ElonMusk OR #SpaceX-filter:retweets'), lang='en').items(15):
        try:
            print("\n Found Tweet by " + "@" + tweet.user.screen_name)
            tweet.favorite()
            print("Liked tweet")
            tweet.retweet()
            print("Retweeted tweet")
        except tweepy.TweepError as error:
            print(error.reason)
            
while True:
    like_and_retweet()
    print("sleeping...")
    time.sleep(30)