from TwitterAPI import TwitterAPI

consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

r = api.request('direct_messages/events/list')

if (r.status_code == 200):

    with open('messagesSent.txt') as my_file:
        messageID_array = my_file.readlines()

    for t in r.json()["events"]:  # For each message
        text_file = open("messagesSent.txt", "a")

        if (str(t["id"] + "\n")) not in messageID_array:
            text_file.write(t["id"] + "\n")
            print("Marked " + t["id"] + " as read.")

        text_file.close()

else:
    print("ERROR GETTING DMS ("+r.status_code+")")

print("Done.")

def markDMasRead(messageID):
    text_file = open("messagesSent.txt", "a")
    text_file.write(messageID + "\n")
    text_file.close()