import datetime
import time
import tweepy


def tweet(message):
  try:
    #@DanielLeeMeeks2
    consumer_key = "U01EcJ8sqBgSaafvPW1u3nHzR"
    consumer_secret = "tt9UdUqKXHVDpJguTyS1fKhTmPxUHq2VRKaqg056ZirIGH3tgA"
    access_key = "3904219755-szrud8F89KgaAPLzjXpKbIWIvVvIqrkeOXLd1vd"
    access_secret = "DBwqE09xXK69tHHlqqv9pFwY0u2V3APoSOjRLVuPJO8Kn"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    ##if (len(message) > 280):
    ##  message = message[0:275] + "...";
    ##  if (len(message) + len(link) + 5 > 280 ):
    ##    message = message[0:280-len(link)-5] + "..."
    api.update_status(status=message)
  except:
    print("There was an error while tweeting.")

while True:
  print(datetime.datetime.now())
  tweet("The time is " + str(datetime.datetime.now()) );
  time.sleep(60)
