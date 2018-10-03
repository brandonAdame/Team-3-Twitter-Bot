#  Tweet from commandline using arguments.
## For easy testing google cloud.
## Not usful for including in project.

from sys import argv
import tweepy

message = argv[1]

try:
        #@3030team3
        consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
        consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
        access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
        access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        if (len(message) > 280):
            message = message[0:275] + "..."
        print(api.update_status(status=message))
        
except:
        print("There was an error while tweeting.")