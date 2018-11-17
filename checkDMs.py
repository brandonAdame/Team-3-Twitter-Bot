from TwitterAPI import TwitterAPI
import requests
import database as database
import time

#@3030team3
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"
twitterID = "1039183691510165505"

api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

def checkDM():
    # Get DMs from last 30 days.
    r = api.request('direct_messages/events/list')

    # Get list of messages that have been read.
    with open('messagesSent.txt') as my_file:
        messageID_array = my_file.readlines()

    print(r.status_code)

    if (r.status_code == 200):
        print(r.json()["events"])
        for t in r.json()["events"]: #For each message
            if (str(t["id"] + "\n")) not in messageID_array:
                if (t["message_create"]["sender_id"] != twitterID):  ##Don't respond to messages sent by ourselve.
                    dmFrom = t["message_create"]["sender_id"]
                    dmTo = t["message_create"]["target"]["recipient_id"]
                    dmMessage = t["message_create"]["message_data"]["text"].encode('ascii', 'ignore').decode('ascii').lower()

                    print(dmFrom + ": " + dmMessage)

                    if (dmMessage[0] == '!'): #If message starts with '!' it is a command
                        command = dmMessage.split(" ", 1)[0].replace("!", "")
                        print("This is a command ("+command+")")
                        if (command == "help"):
                            sendHelp(dmFrom)
                        elif (command == "add"):
                            event = dmMessage.split(" ")
                            print(event)
                            if (event[1] == "localweather"):
                                sendDM(dmFrom, decodeLocalWeather(event, dmFrom))
                            elif (event[1] == "dailyquote"):
                                database.addDailyQuote(dmFrom)
                                sendDM(dmFrom, "You will receive a DM of a quote everyday at 7 AM.")
                            elif (event[1] == "dailystocks"):
                                #TODO
                                sendDM(dmFrom, "Daily Stocks is not done yet.")
                            elif (event[1] == "word"):
                                database.addDailyWord(dmFrom)
                                sendDM(dmFrom, "You will receive a DM of a word everyday at 9 AM.")
                            else:
                                print(sendDM(dmFrom, "Unknown command.  Type !help for more info."))
                #TODO !unsub
                #TODO !unsubAll
                #TODO !info
                #TODO !info [eventID]
                markDMasRead(t["id"])

    else:
        print("There was a problem getting Twitter DMs. (" + str(r.status_code) + ")")

def sendDM(twitterID, message):
    event = '{"event":{"type":"message_create","message_create":{"target":{"recipient_id":"%s"},"message_data":{"text":"%s"}}}}' % (twitterID, message)
    r = api.request('direct_messages/events/new', event)
    print(str(r.status_code) + ": " + message)

def markDMasRead(messageID):
    text_file = open("messagesSent.txt", "a")
    text_file.write(messageID + "\n")
    text_file.close()

def sendHelp(twitterID):
    #TODO Format real command help to fit in a DM.
    sendDM(twitterID, "This Twitter bot is not finished.  Follow @csci3030team3 to be notifyed when it is ready.")

def checkTimeFormat(input):

        timeSplit = input[2].split(":")
        if (len(timeSplit) == 3):
            #TODO Check that things are numbers between 0-23:0-59:0-59
            return True
        else:
            return False

###

def decodeLocalWeather(input, twitterID):
    passTest = True
    '''if (input[0] != "localWeather"):
        return "Input type did not match localWeather."
    else:'''
    if ((len(input) == 3)):
        timeSend = "08:00:00"
        return database.addLocalWeatherEvent(twitterID, input[1], timeSend)
    elif (len(input) == 4):
        if (checkTimeFormat(input[2])):
            timeSend=input[2]
        else:
            timeSend="08:00:00"

        database.addLocalWeatherEvent(twitterID, input[1], timeSend)
        return "localWeather Event added to database."

    else:
        return "Unproperly formatted command: Use !add localWeather [zipCode] [time to send weather, optional]"
    r = database.addLocalWeatherEvent(twitterID, input[1], sendTime).JSON()
    return "localWeather Event ("+r["id"]+") added to database. "

#checkDM()

while True:
    checkDM()
    time.sleep(90)