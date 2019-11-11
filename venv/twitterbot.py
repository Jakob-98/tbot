import tweepy
import os


#import token from token.txt file in same directory
token_file = os.path.join('../', "token.txt")

tokens = open(token_file,'r')

for line in tokens:
    keys = line.split(';')
    CONSUMER_KEY = keys[0]
    CONSUMER_SECRET = keys[1]
    ACCESS_TOKEN = keys[2]
    ACCESS_TOKEN_SECRET = keys[3]


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello world")
