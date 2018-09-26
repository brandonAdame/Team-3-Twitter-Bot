import tweepy

# credentials
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_token = 	"1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_token_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

# login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# autheticating
api = tweepy.API(auth)

print('authentication successful')

phrase = 'get a rain jacket'
api.update_status(phrase)