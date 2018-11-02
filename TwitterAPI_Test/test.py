from TwitterAPI import TwitterAPI
api = TwitterAPI("yVFov91a4AnsnXmbh45MBov9i", "Fb8HDKzUv2sd68nOaJKU2EimlyR97CKjLAYKIyhNvnwG4H094X", "3904219755-6SWMiMku6P6H6r9jv83ql0NQ8TcxIsC8cJfGUUu", "OZzMalAuh3Kn6f2lxdVNU8Q0HjYbmmvoLBG1qt0bh9D62")

r = api.request('direct_messages/events/list')
print(r.status_code)
print(r.json())


##Get DMs
r = api.request('direct_messages/events/show', {'id':'1058223541361926148'})
print(r.status_code)
print(r.json())

## SEND DM
event = '{"event":{"type":"message_create","message_create":{"target":{"recipient_id":"%s"},"message_data":{"text":"%s"}}}}' % (590254391, "test123")
r = api.request('direct_messages/events/new', event)
print(r.status_code)


##Search Tweets
r = api.request('search/tweets', {'q':'weather', 'count':'5'})
for item in r:
        print(item)

#####Tweet something
r = api.request('statuses/update', {'status':'This is a tweet from python! @csci3030team3'})
print(r.status_code)