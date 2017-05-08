## Analysis Sentiment with Python

## Tweets Streaming Usage 
1. Edit config.py with your configuration
```
consumer_key = '<your-consumer-key>'
consumer_secret = '<your-consumer-secret>'
access_token = '<your-access-token>'
access_secret = '<your-access-secret>'
```
2. Create directory for data streaming
```
$ mkdir data_stream
```
3. Run tweets_streaming.py
```
$ python tweets_stream.py -q apple -d data_stream
```