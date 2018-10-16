import  requests

baseURL = "http://scotustoons.com/team3/"

def nextEvent():
    apiURL = baseURL + "index.php"
    next = requests.get(apiURL).json()
    print("Next event happens at " + next["events"][0]["nextRunTime"])
    return next["events"][0]

def getByID(id):
    apiURL = baseURL + "index.php?id=" + str(id)
    event = requests.get(apiURL).json()
    return event["events"][0]

def getByUsername(username):
    apiURL = baseURL + "index.php?twitterAccount=" + username
    events = requests.get(apiURL).json()
    return events["events"]

def addLocalWeatherEvent(twitterAccount, location, sendTime):
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=localWeather&location="+location+"&sendTime="+sendTime
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()
    else:
        return  r.text

def addDailyStocks(twitterAccount, symbol):
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyStocks&symbol="+symbol
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()
    else:
        return  r.text

def addDailyQuote(twitterAccount):
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyQuote"
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()
    else:
        return r.text

def unsub(id):
    apiURL = baseURL + "unsub.php?id="+str(id)
    return requests.get(apiURL).text

def unsubAll(username):
    apiURL = baseURL + "unsub.php?twitterAccount="+username
    return requests.get(apiURL).text

##DEMOS
print("\nDemos\n")

##GET/LOOKUP
print("NEXT: " + str(nextEvent()))
print("GETBYID(1): " + str(getByID(1)))
print("getByUsername(DanielLeeMeeks): " + str(getByUsername("DanielLeeMeeks")))
print("")

##CREATE NEW EVENTS
print("addLocalWeatherEvent(\"DanielLeeMeeks2\", \"27834\", \"20:00:00\"): " + str(addLocalWeatherEvent("DanielLeeMeeks2", "27834", "20:00:00")))
print("addDailyStocks(\"DanielLeeMeeks2\", \"ATT\"): " + str(addDailyStocks("DanielLeeMeeks2", "ATT")))
print("addDailyQuote(\"DanielLeeMeeks2\"): " + str(addDailyQuote("DanielLeeMeeks2")))
print("")

#DELETING EVENTS (Uncomment these and change parameters to test.)
#print("Remove an event by ID, unsub(24): " + str(unsub(24)))
#print("Remove all events a user is signed up for, unsubAll(\"DanielLeeMeeks2\"): " + str(unsubAll("DanielLeeMeeks2")))