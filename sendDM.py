from TwitterAPI import TwitterAPI
import pause
import requests
import database as database
import datetime
import getDailyQuote as getDailyQuote
#import checkDMs as checkDMs
import weather as weather
import getWordOfDay as word
import traceback
import sys
import time

#@3030team3
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"
twitterID = "1039183691510165505"
MAX_SLEEP_TIME_BETWEEN_EVENTS = 5 #Event if an event is longer than this time away, the script will recheck for newer events after this minutes.

api = TwitterAPI(consumer_key, consumer_secret, access_key, access_secret)

tryCounter = 0

def tick():
    global tryCounter
    tryCounter = tryCounter + 1
    print("Next event triggers at " + str(getNextTime()))
    pause.until(getNextTime())
    event = database.nextEvent()
    print(event)
    try:
        if (event["eventType"] == "localWeather"):
            print(event["location"])
            sendDM(event["twitterAccount"], weather.getWeather(event["location"]))
            database.updateEventTimeAuto(event["id"])
            print("Run localWeather event #" + event["id"])
        elif (event["eventType"] == "dailyStock"):
            #TODO Call dailyStock function
            print("Run dailyStock #" + event["id"])
        elif (event["eventType"] == "dailyQuote"):
            print(int(event["twitterAccount"]))
            sendDM(event["twitterAccount"], getDailyQuote.get_daily_quote("https://www.brainyquote.com/quote_of_the_day").encode('ascii', 'ignore').decode('ascii').replace('\n', ""))
            database.updateEventTimeAuto(event["id"])
            print("Run daily quote #" + event["id"])
        elif (event["eventType"] ==  "dailyWord"):
            sendDM(event["twitterAccount"], word.getWordOfDay())
            database.updateEventTimeAuto(event["id"])
            print("Run word event #" + event["id"])

        tryCounter = 0

    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print(lines)
        if tryCounter <= 3:
            time.sleep(10)
        else:
            database.updateEventTimeAuto(event["id"])
            print("Event #" + event["id"] + " failed 3 times.  It was skipped.")


#TODO Don't let program sleep for 6+ hours because any new things scheduled during that time will not run until the next day
def getNextTime():
    n = database.nextEvent()["nextRunTime"]
    nextEventDate = n.split(" ")[0];
    nextEventTime = n.split(" ")[1];

    n_year = int(nextEventDate.split("-")[0])
    n_mon = int(nextEventDate.split("-")[1])
    n_day = int(nextEventDate.split("-")[2])

    n_hour = int(nextEventTime.split(":")[0])
    n_min = int(nextEventTime.split(":")[1])
    n_sec = int(nextEventTime.split(":")[2])

    nextDate = datetime.datetime(n_year, n_mon, n_day, n_hour, n_min, n_sec)

    if ((nextDate > datetime.datetime.now()+datetime.timedelta(minutes=MAX_SLEEP_TIME_BETWEEN_EVENTS))):
        nextDate = datetime.datetime.now() + datetime.timedelta(minutes = MAX_SLEEP_TIME_BETWEEN_EVENTS)

    return nextDate

def sendDM(twitterID, message):
    event = '{"event":{"type":"message_create","message_create":{"target":{"recipient_id":"%s"},"message_data":{"text":"%s"}}}}' % (twitterID, twitterStringCleaner(message))
    r = api.request('direct_messages/events/new', event)
    print(str(r.status_code) + ": " + message)

def twitterStringCleaner(input):
    output = input.replace('\r', ' ').replace('\n', ' ').replace('"', '\'').replace('\\', ' ').replace('-', ' ')
    return output

#print ()
#getNextTime()
while True:
    tick()

