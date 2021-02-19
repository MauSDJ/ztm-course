import tweepy
import time

auth = tweepy.OAuthHandler('25pORjHNuDz893Ggo9CFwyVoI', 'ORNtm8llKTqrJKY7e0HAdmqsSns0y3JobBsNuVb1Nm4dp5P5hU')
auth.set_access_token('1324059127778287616-O505y69KbtVznpUnAm50nkigpQ3A92', 'jtub9FIwPB5y3KkKKz4SS1Cx6DhOmkvciAYuKt22tKWKu')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(1000)

""" for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  follower.follow()
  break """

search_string = 'python'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
  try:
    tweet.favorite()
    print('I liked that tweet')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break