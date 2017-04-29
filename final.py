 


import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
consumer_key = 'Eq9GkklM6mOKSa06CHqP28IJE'
consumer_secret = 'M1R8L6DpkZbbPplmsYARgHngPUGjraOgJks0ZPp0IlijHHQAbo'
access_token = '751711219929718788-h0uIzkLzkOItPNVWO3q4EF5J2nx39Hu'
access_secret = 'yonHkLR57hp3nEQUg0efhYYP2awzeY61Y2TRTSuUUBuuG'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    print(status.text)
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on_data: '+str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
