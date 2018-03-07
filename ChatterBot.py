# Create a function that tweets
# Dependencies
import tweepy
import json
import time

# Twitter API Keys
import os
"""
consumer_key = os.getenv("twitter_consumer_key")
consumer_secret = os.getenv("twitter_consumer_secret")
access_token = os.getenv("twitter_access_token")
access_token_secret = os.getenv("twitter_access_token_secret")
"""

consumer_key = "ThPe6egpT3OJCiRfx7w7lGyVH"
consumer_secret = "EnGwBptSnjSKEjgIbOi3D4qtRvfjcgnCWm3pDGQscjs07qXbG2"
access_token = "969396072215818240-ZVyRxct50k8giGAXzKoAVd4uThbuxSu"
access_token_secret = "tgyVOelmg2LN0FdlbrW37rh55DvMtWzwxj7oQtYRkBy81"


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(f"practice tweet from python script deployed to heroku: #{tweet_number}!")

# Create a function that calls the TweetOut function every minute
counter = 0

t_end = time.time() + 60 * 5
while(time.time() < t_end):
    TweetOut(counter)
    time.sleep(60)
    counter = counter + 1
