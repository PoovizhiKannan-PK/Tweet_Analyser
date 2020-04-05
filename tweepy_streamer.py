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
#sys.stdout = codecs.getwriter('utf8')(sys.stdout)

class TwitterClient():
	"""
	This class in used to implement Cursor function of tweepy
	"""
	def __init__(self, twitter_user= None):
		self.auth = TwitterAuthenticator().authenticate_twitter_app()
		self.twitter_client = API(self.auth)
		self.twitter_user  ="realDonaldTrump"

	def get_twitter_client_api(self):
		# This method just returns the twitter_client variable created in the above method
		return self.twitter_client

	'''
	 Here Cursor function has three parameters.
	1. User_timeline which specifies that the twwwtss are fetched from the user specified. If not specified, it takes the default value which
	   is null, which means the tweets are fetched from your own account
    2. Items parameter which speifies the number of tweets to be fetched.
	3. id specifies the user
	'''
	def get_user_timeline_tweets(self, num_tweets):
		tweets = []
		# user_timeline is function to get tweets posted by the user
		for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
			tweets.append(tweet)
		return tweets

	def get_friend_list(self, num_tweets):
		friend_list = []
		# .followers specifies the followers
		for friend in Cursor(self.twitter_client.followers, id= self.twitter_user).items(num_tweets):
			friend_list.append(friend)
		return friend_list

	def get_home_timeline_tweets(self, num_tweets):
		home_tweets = []
		# .home_timeline means the tweets in the home page of the user specified
		for htweets in Cursor(self.twitter_client.home_timeline, id = self.twitter_user).items(num_tweets):
			home_tweets.append(htweets)
		return home_tweets

class TwitterAuthenticator():
	def authenticate_twitter_app(self):
		#Below code authenticates the credentials and pass the hashtags for the tweets to be fetched
		auth = OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_SECRET)
		auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
		return auth

class TwitterStreamer():
	"""
	This class is user defined
	This if for streaming and processing live tweets
	"""
	def __init__(self):
		# creating an object for TwitterAuthenticator() class
		self.twitter_authenticator= TwitterAuthenticator()

	def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
		listener = TwitterListener(fetched_tweets_filename)
		# Using the object of TwitterAuthenticator class to call its function
		auth = self.twitter_authenticator.authenticate_twitter_app()
		stream=Stream(auth, listener)
		stream.filter(track=hash_tag_list)



class TwitterListener(StreamListener):

	"""
	on_data listens to the data from StreamListener
	on_error prints the error
	These are inbluit functions which we are overwriting
	"""
	def __init__(self, fetched_tweets_filename):
		#This is a constructor
		self.fetched_tweets_filename=fetched_tweets_filename


	"""
	Here "data" is the tweets read by stream listener
	# data is appaended in the file name specified by self.fetched_tweets_filename
	To append data, the mode is set as "a"
	"""
	def on_data(self,data):

		try:
			print(data,'\n')
			with open(self.fetched_tweets_filename,'a')	as fetched_tweet:
				fetched_tweet.write(data)
			return True
		except BaseException as e:
			print("Error on data : %s" %str(e))
		return True


	def on_error(self, status):
		if status == 420:
			#Returninh flase on_data method, if the error '420' occours, which in case not noticed may
			#lead to blocking of your API
			return false;
		print(status)


class TwitterAnalyzer():
	"""
	Funtionality for analyzing and catecorizing content from tweets
	"""
	pass

if __name__ == "__main__":
	twitter_client = TwitterClient()
	api=twitter_client.get_twitter_client_api()
	#user_timeline is fuction from twitter_client. This function aloows to get tweets from user User_timeline
	#and specify the username and number of tweets
	#screen name is the user name
	#count = no of tweets
	tweets=[]
	for tweet in api.user_timeline(screen_name="realDonaldTrump", count=2):
		tweets.append(tweet)
	print("lalalalala   ",tweets,"\n")
