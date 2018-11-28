from TwitterAPI import TwitterAPI
import requests
import database as database
import time
import traceback
import sys

#@3030team3
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"
twitterID = "1039183691510165505"
SLEEP_BETWEEN_CHECKING_DMS = 90 #How many seconds to wait between get DM request (MINIMUM = 60).

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
                    try:
                        dmFrom = t["message_create"]["sender_id"]
                        dmTo = t["message_create"]["target"]["recipient_id"]
                        dmMessage = t["message_create"]["message_data"]["text"].encode('ascii', 'ignore').decode('ascii').lower()

                        print(dmFrom + ": " + dmMessage)

                        if (dmMessage[0] == '!'): #If message starts with '!' it is a command
                            command = dmMessage.split(" ", 1)[0].replace("!", "")
                            print("This is a command ("+command+")")
                            if (command == "help"):
                                event = dmMessage.split(" ")
                                if (int(len((event))<1)):
                                    if event[1] == "eventTypes":
                                        sendEventHelp(dmFrom)
                                    else:
                                        sendHelp(dmFrom)
                                else:
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
                                    print(sendDM(dmFrom, "Unknown add command.  Type !help for more info."))
                            elif (command == "unsuball"):
                                sendDM(dmFrom, database.unsubAll(dmFrom))
                            elif (command == "unsub"):
                                #TODO !unsub
                                print("not done")
                            elif (command == "info"):

                                if (len(dmMessage.split(" ")) > 1):
                                    print(dmMessage.split(" ")[1])
                                    sendDM(dmFrom, eventToString(database.getByID(dmMessage.split(" ")[1])))
                                    #TODO !info [eventID]
                                else:
                                    sendDM(dmFrom, "LIST OF YOUR EVENTS:")
                                    print(len(dmMessage.split(" ")))
                                    events = database.getByUsername(dmFrom)
                                    for e in events:
                                        print(eventToString(e))
                                        sendDM(dmFrom, eventToString(e))
                            else:
                                sendDM(dmFrom, "Sorry, we do not understand the command " + command + ".  Use !help for a list of commands.")
                                database.addMessage("checkDM.py", "error", "Unknown command: " + command)
                    except Exception:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
                        e = ""
                        for l in lines:
                            e = e + ".  " + l
                        sendDM(dmFrom, "There was an error processing your DM. ("+twitterStringCleaner(e)+")")
                        database.addMessage("checkDM.py", "error", "There was a problem processing a DMs. (" + str(r.status_code) + ")")
                markDMasRead(t["id"])

    else:
        print("There was a problem getting Twitter DMs. (" + str(r.status_code) + ")")
        database.addMessage("checkDM.py", "error", "There was a problem getting Twitter DMs. (" + str(r.status_code) + ")")

    database.addMessage("checkDM.py", "online", "Script checkDM.py is still working.")

def eventToString(event):
    ret = "Event #" + event["id"] + " is an " + event["eventType"] + " event."
    if (event["eventType"] == "localWeather"):
        ret = ret + "  This event send the weather for " + event["location"] + "  every day at " + event["sendTime"] + "."
    elif (event["eventType"] == "dailyWord"):
        ret = ret + "  This event sends a word every day at 9:00:00."
    elif (event["eventType"] == "dailyQuote"):
        ret = ret + "  This event sends a quote every day at 7:00:00."
    elif (event["eventType"] == "dailyStocks"):
        ret = ret + "  This event sends the stock value of " + event["symbol"] + " every day at 17:30:00."

    return ret

def sendDM(twitterID, message):
    event = '{"event":{"type":"message_create","message_create":{"target":{"recipient_id":"%s"},"message_data":{"text":"%s"}}}}' % (twitterID, message)
    r = api.request('direct_messages/events/new', event)
    print(str(r.status_code) + ": " + message)
    print(database.addMessage("checkDMs.py", "sent", "User " + twitterID + " was sent: " + message))

def markDMasRead(messageID):
    text_file = open("messagesSent.txt", "a")
    text_file.write(messageID + "\n")
    text_file.close()

def sendHelp(twitterID):
    #TODO Format real command help to fit in a DM.
    sendDM(twitterID, "NOTE: This Twitter bot is not finished and may be unstable.  Follow @csci3030team3 to be notifyed when it is ready.")
    sendDM(twitterID, "Add a new event by sending '!add [eventType] [parameters1] [parameters2]...'  Type !help eventTypes for a list of events.")
    sendDM(twitterID, "See a list of the events you are signed up for by sending '!info'")
    sendDM(twitterID, "Unsubscribe from an event by sending '!unsub [eventID]' or unsubscribe from all events by sending '!unsubAll'")
    print(database.addMessage("checkDMs.py", "received", "User " + twitterID + " asked for help."))
    ##print(database.addMessage("checkDMs.py", "sent", "User " + twitterID + " was sent help."))

def sendEventHelp(twitterID):
    sendDM(twitterID, "Types of events:")
    sendDM(twitterID, "LOCAL WEATHER: Sends the local weather at the time you want (defalt 8AM).  '!add localWeather [zipCode] [time to send weather, formatted HH:MM:SS (24 hour time).  optional]'")
    sendDM(twitterID, "DAILY QUOTE*: Sends a daily quote every morning at 7AM.  '!add dailyQuote'")
    sendDM(twitterID, "DAILY STOCK: Send the value of a stock everyday after the stock market cloeses (5:30PM).  '!add dailyStocks [stock symbol]'")
    sendDM(twitterID, "WORD OF THE DAY: Sends a daily word every morning at 9AM.  '!add word'")
    print(database.addMessage("checkDMs.py", "received", "User "+twitterID+" asked for event help."))
    ##print(database.addMessage("checkDMs.py", "sent", "User " + twitterID + " was sent event help."))

def checkTimeFormat(input):

        timeSplit = input.split(":")
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
    print(len(input))
    if ((len(input) == 3)):
        timeSend = "08:00:00"
        return database.addLocalWeatherEvent(twitterID, input[2], timeSend)
    elif (len(input) == 4):
        if (checkTimeFormat(input[3])):
            timeSend=input[3]
        else:
            timeSend="08:00:00"
        database.addLocalWeatherEvent(twitterID, input[2], timeSend)
        return "localWeather Event added to database."

    else:
        return "Unproperly formatted command: Use !add localWeather [zipCode] [time to send weather, optional]"
    r = database.addLocalWeatherEvent(twitterID, input[2], sendTime).JSON()
    print(input[2])
    ##print(database.addMessage("database.py", "received", "Added weather event to database: " + r["events"][0]["id"]))
    return "localWeather Event ("+r["id"]+") added to database. "

def twitterStringCleaner(input):
    return input.replace('\r', ' ').replace('\n', ' ').replace('"', '\'').replace('\\', ' ')

#checkDM()
while True:
    checkDM()
    time.sleep(SLEEP_BETWEEN_CHECKING_DMS)

