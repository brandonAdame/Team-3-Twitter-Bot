import feedparser
import time
import datetime
import tweepy
import requests
##Get weather alerts from The National Weather Service once a minute.  If they are new, it prints them to the consolse otherwise it skips them.

tweetSkipper = True;

def tweet(message, link):
    try:
        #@DanielLeeMeeks2
        consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
        consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
        access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
        access_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        if (len(message) > 280):
            message = message[0:275] + "...";
        if (len(message) + len(link) + 5 > 280 ):
            message = message[0:280-len(link)-5] + "..."
        api.update_status(status=message + "\n" + link)
        print(message)
    except:
        print("There was an error while tweeting.")



while True:

    ##get weather Alerts from The National Weather Service
    ##https://alerts.weather.gov/
    ##weatherAlerts = feedparser.parse("https://alerts.weather.gov/cap/us.php?x=0")
    weatherAlerts = feedparser.parse("https://alerts.weather.gov/cap/wwaatmget.php?x=NCC147&y=0")
    #weatherAlerts = feedparser.parse("https://alerts.weather.gov/cap/nc.php?x=0")

    ##print(weatherAlerts.entries[1].keys())

    ##Open list of alerts that have already been seen
    with open('alertList.txt') as my_file:
        alert_array = my_file.readlines()

    count_skipped = 0
    count_alerted = 0

    print(weatherAlerts)

    ##Look at every item in the alerts rss feed.
    for entry in weatherAlerts.entries:
        ##if the item is new add the item to the alerts list and print data about it.
        #print(entry.id)
        if (entry.id != "https://alerts.weather.gov/cap/wwaatmget.php?x=NCC147&y=0"):
            if (entry.id + "\n") not in alert_array:
                print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] (" + entry.title + ") " + entry.summary)
                if (tweetSkipper):
                    tweet(entry.summary, entry.link)
                else:
                    print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] This is the first load, nothing will be tweeted.")
                    tweetSkipper = True
                text_file = open("alertList.txt", "a")
                text_file.write("\n" + entry.id)
                text_file.close()
                count_alerted += 1
            ##if the item is old skip it
            else:
                ##print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] Alert ID " + entry.id + " has already ran and will be skipped.")
                count_skipped += 1
        else:
            print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] There are no active watches, warnings or advisories")

    #print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] "+str(count_alerted) + " new alerts found.")
    #print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] " + str(count_skipped) + " old alerts skipped.\n")

    #id = weatherAlerts.entries[i].id
    #published = weatherAlerts.entries[i].published
    #title = weatherAlerts.entries[i].title
    #update = weatherAlerts.entries[i].update
    #summary = weatherAlerts.entries[i].summary
    #event = weatherAlerts.entries[i].cap_event
    #severity = weatherAlerts.entries[i].cap_severity
    #expires = weatherAlerts.entries[i].cap_expires

    #print(title)

    #wait a minute before running again
    i = 6;
    while i > 0:
        #print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] Will check for new alerts in " + str(i*10) + " seconds.")
        time.sleep(10)
        i -= 1;




