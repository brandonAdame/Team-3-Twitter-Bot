import  requests

baseURL = "http://scotustoons.com/team3/"

def nextEvent():
    """
    Returns the next event to be ran.  If the time an event should have ran has already passed, that event is returned.

    Returns
    -------
    dict
        a dict of the next event to be ran.
    """
    apiURL = baseURL + "index.php"
    next = requests.get(apiURL).json()
    print("Next event happens at " + next["events"][0]["nextRunTime"])
    return next["events"][0]

def getByID(id):
    """
    Returns the event with the id given.

    Parameters
    ----------
    id : int
        The ID number of the event you are looking up.

    Returns
    -------
    dict
        a dict of the next event you looked up.
    """
    apiURL = baseURL + "index.php?id=" + str(id)
    event = requests.get(apiURL).json()
    return event["events"][0]

def getByUsername(username):
    """
    Returns an array of events that a user has signed up for.

    Parameters
    ----------
    username : str
        Twitter username of a user to look up.

    Returns
    -------
    list
        Events that a user has signed up for.
    """
    apiURL = baseURL + "index.php?twitterAccount=" + username
    events = requests.get(apiURL).json()
    return events["events"]

def addLocalWeatherEvent(twitterAccount, location, sendTime):
    """
    Add a new localWeather Event to the database.

    Parameters
    ----------
    twitterAccount : str
        Twitter username of a user the event will be sent to.
    location : str
        Location the weather forcast will be from.
    sendTime : str
        The time the weather report should be sent.  Formatted "HH:MM:SS"

    Returns
    -------
    dict
        localWeather event that was just created.
    """
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=localWeather&location="+location+"&sendTime="+sendTime
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()["events"][0]
    else:
        return  r.text

def addDailyStocks(twitterAccount, symbol):
    """
    Add a new dailyStocks event to the database.

    Parameters
    ----------
    twitterAccount : str
        Twitter username of a user the event will be sent to.
    symbol : str
        The stock symbol of the stock the user wants to be messaged about, example: MMM, ATT

    Returns
    -------
    dict
        dailyStock event that was just created.
    """
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyStocks&symbol="+symbol
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()["events"][0]
    else:
        return  r.text

def addDailyQuote(twitterAccount):
    """
    Add a bew dailyQuote event to the database.

    Parameters
    ----------
    twitterAccount : str
        Twitter username of a user the event will be sent to.

    Returns
    -------
    dict
        dailyStock event that was just created.
    """
    apiURL = baseURL + "add.php?twitterAccount="+twitterAccount+"&eventType=dailyQuote"
    r = requests.get(apiURL)
    if (r.text != "Unknown event type.  Did not add to database."):
        return r.json()["events"][0]
    else:
        return r.text

def unsub(id):
    """
    Delete event from the database by id.

    Parameters
    ----------
    id : int
        id number of the event to be deleted.

    Returns
    -------
    str
        Message telling you the event has been deleted.

    """
    apiURL = baseURL + "unsub.php?id="+str(id)
    return requests.get(apiURL).text

def unsubAll(username):
    """
    Delete all events from the database a user is signed up for.

    Parameters
    ----------
    username : str
        Username who's events will be deleted.

    Returns
    -------
    str
        Message telling you the event(s) that have been deleted.

    """
    apiURL = baseURL + "unsub.php?twitterAccount="+username
    return requests.get(apiURL).text

def updateEventTimeAuto(id):
    """
    Updates the lastRunTime and nextRunTime in the database.  Call this (or updateEventTime() ) when you send an event

    Parameters
    ----------
    id : int
        ID number of the event that was sent.

    Returns
    -------
    dict
        Updated event.
    """
    apiURL = baseURL + "run.php?id=" + str(id)
    r = requests.get(apiURL)
    return r.json()["events"][0]

def updateEventTime(id, nextSendTime):
    """
    Updates the lastRunTime and nextRunTime to a specified time in the database.  Call this (or updateEventTimeAuto() ) when you send an event

    Parameters
    ----------
    id : int
        ID number of the event that was sent.
    nextSendTime : str
        The time the event should be ran next.  Formatted "YYYY-MM-DD HH:MM:SS".

    Returns
    -------
    dict
        Updated event.
    """
    apiURL = baseURL + "run.php?id=" + str(id) + "&nextSendTime=" + nextSendTime
    r = requests.get(apiURL)
    return r.json()["events"][0]

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


##Updating Next/Last send time
print("updateEventTime(1): " + str(updateEventTimeAuto(1)))
print("updateEventTime(1), \"2020-01-01 08:00:00\"): " + str(updateEventTime(1, "2020-01-01 08:00:00")))
print("")

#DELETING EVENTS (Uncomment these and change parameters to test.)
#print("Remove an event by ID, unsub(24): " + str(unsub(24)))
#print("Remove all events a user is signed up for, unsubAll(\"DanielLeeMeeks2\"): " + str(unsubAll("DanielLeeMeeks2")))