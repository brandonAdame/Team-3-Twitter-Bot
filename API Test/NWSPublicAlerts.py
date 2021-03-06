import feedparser
import time
##Get weather alerts from The National Weather Service one a minute.  If they are new print them to the consolse otherwise skip them.

while True:

    ##get weather Alerts from The National Weather Service
    ##https://alerts.weather.gov/
    weatherAlerts = feedparser.parse("https://alerts.weather.gov/cap/us.php?x=0")
    ##weatherAlerts = feedparser.parse("https://alerts.weather.gov/cap/wwaatmget.php?x=NCC147&y=0")

    ##print(weatherAlerts.entries[1].keys())

    ##Open list of alerts that have already been seen
    with open('alertList.txt') as my_file:
        alert_array = my_file.readlines()

    count_skipped = 0
    count_alerted = 0

    ##Look at every item in the alerts rss feed.
    for entry in weatherAlerts.entries:
        ##if the item is new add the item to the alerts list and print data about it.
        if (entry.id + "\n") not in alert_array:
            print("[" + entry.cap_event + "] " + entry.summary)
            text_file = open("alertList.txt", "a")
            text_file.write("\n" + entry.id)
            text_file.close()
            count_alerted += 1
        ##if the item is old skip it
        else:
            ##print("Alert ID " + entry.id + " has already ran and will be skipped.")
            count_skipped += 1

    print("\n"+str(count_alerted) + " new alerts found.")
    print(str(count_skipped) + " old alerts skipped.\n")

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
        print("Will check for new alerts in " + str(i*10) + " seconds.")
        time.sleep(10)
        i -= 1;
