import tweepy
import os



#import token from token.txt file in same directory
token_file = os.path.join(path, "token.txt")

with open(token_file, 'rb') as f:
    token = f.read().replace('\n', '')

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello world")