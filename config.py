from tweepy import OAuthHandler

# Fill the variable below with your key
# if you not have you, can create app first in https://apps.twitter.com/
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)