import tweepy

twitter_auth_keys = {
    "consumer_key" : "YOUR_CONSUMER_KEY",
    "consumer_secret" : "YOUR_CONSUMER_SECRET",
    "access_token" : "YOUR_ACCESS_TOKEN",
    "access_token_secret" : "YOUR_ACCESS_TOKEN_SECRET"
}

auth = tweepy.OAuthHandler(
    twitter_auth_keys['consumer_key'],
    twitter_auth_keys['consumer_secret']
)
auth.set_access_token(
    twitter_auth_keys['access_token'],
    twitter_auth_keys['access_token_secret']
)

api = tweepy.API(auth)

tweet = "This is just my first post using the twitter dev API! :)"
status = api.update_status(status=tweet)