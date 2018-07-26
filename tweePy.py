import tweepy
from tweepy import OAuthHandler

consumer_key = 'HazS6yUXLkJ3UkosVpJqdHPPK'
consumer_secret = 'oDk35v7aZmYwdzJY8mS6xyC7idl7Rk9ZvQrPj4f8tz59ek5G5u'
access_token = '4277411712-INkdY7s9cnHyBMKK4vMFmNU5DG1A7xqSyE6DSyr'
access_secret = 'NSNWi5LQ6fLTUDb6udCAd5cnecA7K4FvFOsgMqxOCMJGv'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)