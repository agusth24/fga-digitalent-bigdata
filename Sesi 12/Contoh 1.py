# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:27:26 2019

@author: ROG-GL553VD
"""

import tweepy
import json

ACCESS_TOKEN = '107282554-vCjzS0Xvdb5h6xnEUYu67mFTUaaUuCPVxCQ2sucd'
ACCESS_SECRET = 'bt6KXJd6Jfo4qWgoImEZtjiZ7zBk3dF103arwxAUWOljE'
CONSUMER_KEY = 'u83fQzGVBzGsWbMYEQ3oAwPL1'
CONSUMER_SECRET = 'rqckM2STaYLQ7RvI3JedImh2tKXeeWzuuzImKObSjAAoApbkkE'

def connect_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth)
    return api

def process_or_store(tweet):
    print(json.dumps(tweet))

api = connect_twitter_OAuth()
public_tweets = api.home_timeline()
for tweet in public_tweets:
    #print(tweet.entities)
    if 'media' in tweet.entities:
        #print(tweet.entities['media'])
        for media in tweet.entities['media']:
            if 'media_url' in media:
                print(media['media_url'])
                print()

countSource = {}
public_tweets2 = api.home_timeline()
for tweet2 in public_tweets2:
    print(tweet2.source)
    if tweet2.source in countSource:
        countSource[tweet2.source] += 1
    else:
        countSource[tweet2.source] = 1

print(countSource)

for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)

for tweet in tweepy.Cursor(api.user_timeline).items(10):
    process_or_store(tweet._json)