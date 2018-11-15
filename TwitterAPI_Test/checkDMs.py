from TwitterAPI import TwitterAPI

#@3030team3
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"
twitterID = "1039183691510165505"

api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)


#Get DMs from last 30 days
r = api.request('direct_messages/events/list')
print(r.status_code)
#print(r.json())

##for message in r.json():
print (r.json()["events"][0]["u'message_create"])
