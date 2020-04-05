from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener  #allow us to listen to tweets based on hastags
from tweepy import OAuthHandler # to authenticate based on keys
from tweepy import Stream

import numpy as np
import pandas as pd
import Credentials
import sys
import codecs


class TwitterClient():
	"""
	This class in used to implement Cursor function of tweepy
	"""
	def __init__(self, twitter_user = None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		self.twitter_user = twitter_user

	def get_twitter_client_api(self):
		# This method just returns the twitter_client variable created in the above method
		return self.twitter_client

class TwitterAuthenticator():
	def authenticate_twitter_app(self):
		#Below code authenticates the credentials and pass the hashtags for the tweets to be fetched
		auth = OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_SECRET)
		auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
		return auth


class TwitterAnalyzer():
	"""
	Funtionality for analyzing and catecorizing content from tweets
	"""
	def tweets_to_df(self, tweets):
		'''
		Create a dataframe using pd.DataFrame() method
		Extract info from tweets using their attribute names like 	text, id, created_at, 
		source(It means from windows or iphone or android), favourite count(likes), retweets count.
		These attribte names can be found using the statement 'print(dir(tweets[0]))'
		'''
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		df['id'] = np.array([tweet.id for tweet in tweets])
		df['tweetlen'] = np.array([len(tweet.text) for tweet in tweets])
		df['date'] = np.array([tweet.created_at for tweet in tweets])
		df['source'] = np.array([tweet.source for tweet in tweets])
		df['like'] = np.array([tweet.favorite_count for tweet in tweets])
		df['retweetcount'] = np.array([tweet.retweet_count for tweet in tweets])
		return df


if __name__ == "__main__":
	twitter_client = TwitterClient()
	tweet_analyser = TwitterAnalyzer()

	api=twitter_client.get_twitter_client_api()
	#user_timeline is fuction from twitter_client. This function aloows to get tweets from user User_timeline
	#and specify the username and number of tweets
	#screen name is the user name
	#count = no of tweets
	tweets = api.user_timeline(screen_name="realDonaldTrump", count=20)
	
	#print(dir(tweets[0]))
	#print(tweets[0].retweet_count)
	df= tweet_analyser.tweets_to_df(tweets)
	print(df.head(10))
