import json
import config
import tweepy
from tweepy.streaming import StreamListener


def process_or_store(data):
    print(json.dumps(data))


api = tweepy.API(config.auth)

# Get status from 
# your timeline account, your friends, and tweet from your friends
# and display data with json format
for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)