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
        #print(data)
        try:
            datas = json.loads(data)
            print(datas)
            #print(datas['entities'])
            #for datas2 in datas['entities']:
                #print(datas2)
            #if 'media' in datas.entities:
            #print(tweet.entities['media'])
                #for media in datas.entities['media']:
                    #if 'media_url' in media:
                        #print(media['media_url'])
                        #print()
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#'])
