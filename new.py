
import re

tweet="e122324$%^&@*&*(#)(rqwjn@##$%q93noi3i390f 32n3jr3092j3oijnfijn3932  329fne9"
class TwitterAnalyzer():

	

	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


ctweet = TwitterAnalyzer()
a = ctweet.clean_tweet(tweet)
print(a)
