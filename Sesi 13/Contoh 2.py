# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:22:46 2019

@author: ROG-GL553VD
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

class MyListener(StreamListener):
 
    def on_data(self, data):
        print(data)
        try:
            with open('senin.json', 'a') as f:
                f.write(json.dumps(json.loads(data),indent=4,sort_keys=True))
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#senin'])
