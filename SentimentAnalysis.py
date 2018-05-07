import tweepy
from textblob import TextBlob

consumer_key = "543VwZwug3IAGHC0A0CgvIfTY"
consumer_secret = "4g3NoSSekKsPj1PAnjw2xxc2cWaOr4hHCSZMhjJNYZL2K9dF4A"
access_token = "218526626-1v478oaSn6GmypDDhyACR807vtyJbrFLK8cyG2H4"
access_token_secret = "1DqI6mrpZlzx0j0O8OBaMBLYDs9qVEUqaRuNZuVEX4AhG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Feminism')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
