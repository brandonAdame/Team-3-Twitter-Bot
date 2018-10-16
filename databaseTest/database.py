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
    ##apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=localWeather&location="+location+"&sendTime="+sendTime
    return "not done, nothing was added to the database."

def addDailyStocks(twitterAccount, symbol):
    ##apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyStocks&symbol="+symbol
    return "not done, nothing was added to the database."

def addDailyQuote(twitterAccount):
    ##apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyQuote"
    return "not done, nothing was added to the database."

def unsub(id):
    ##apiURL = baseURL + "unsub.php?id="+id
    return "not done, nothing was added to the database."

def unsubAll(username):
    ##apiURL = baseURL + "unsub.php?twitterAccount="+username
    return "not done, nothing was added to the database."

##DEMOS
print("\nDemos\n")

##GET/LOOKUP
print("NEXT: " + str(nextEvent()))
print("GETBYID(1): " + str(getByID(1)))
print("getByUsername(DanielLeeMeeks): " + str(getByUsername("DanielLeeMeeks")))
print("")

##CREATE NEW EVENTS
print("addLocalWeatherEvent(\"DanielLeeMeeks2\", \"27834\", \"20:00:00\"): " + addLocalWeatherEvent("DanielLeeMeeks2", "27834", "20:00:00"))
print("addDailyStocks(\"DanielLeeMeeks2\", \"ATT\"): " + addDailyStocks("DanielLeeMeeks2", "ATT"))
print("addDailyQuote(\"DanielLeeMeeks2\"): " + addDailyQuote("DanielLeeMeeks2"))
print("")

#DELETING EVENTS
print("Remove an event by ID, unsub(1): " + unsub(1))
print("Remove all events a user is signed up for, unsubAll(\"DanielLeeMeeks\"): " + unsubAll("DanielLeeMeeks"))