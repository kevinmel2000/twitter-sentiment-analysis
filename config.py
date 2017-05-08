from tweepy import OAuthHandler

# Fill the variable below with your key
# if you not have you, can create app first in https://apps.twitter.com/
consumer_key = '2LxBOLqDuyRDVN05yQ5LGgfMY'
consumer_secret = 'WihTd3MLzD026OkiuCI2bnnbqF5eSF9Fwv5gyLAdgpxjq3WAkv'
access_token = '713569592312860672-pZDxV2vRFrW6qbfGG3v90CeJpUNZM4A'
access_secret = 'OiaN8kNfZEeMoMaqcs5GSYkfNyU2uJiJ28a7oolSy8NU4'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)