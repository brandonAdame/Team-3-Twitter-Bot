# -*- coding: utf-8 -*-
# =========================================================================================
#                                     Imports
# =========================================================================================
import requests  # Python HTTP for Humans.
import feedparser  # Parse RSS Feeds
import time  # Time and Converting.
import tweepy  # Twitter API
import zipcodes  # zipcodes database
import schedule  # API for Schedulng jobs.
import datetime  # Manipulating Dates
from datetime import date
import calendar
from requests import get  # Send HTTP Requests.
from bs4 import BeautifulSoup
import database as database

# =========================================================================================
#                                     API Keys
# =========================================================================================
# OpenWeatherMap Key
apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

# Twitter keys (@CSCIteam3)
twitter_consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
twitter_consumer_key_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
twitter_access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
twitter_access_key_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

# Tweepy authentication
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_key_secret)
auth.set_access_token(twitter_access_key, twitter_access_key_secret)
api = tweepy.API(auth)

# Daily quote url
url = "https://www.brainyquote.com/quote_of_the_day"


# =========================================================================================
#                                     get_soup
# =========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
# -----------------------------------------------------------------------------------------
def get_soup(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup


# =========================================================================================
#                            get_len_quote_containers
# =========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
# -----------------------------------------------------------------------------------------

def get_len_quote_containers(url):
    html_soup = get_soup(url)

    # gets types of quotes available
    quote_containers = html_soup.find_all('h2', class_='qotd-h2')
    print(quote_containers)  # displays categories of quotes

    return len(quote_containers)


# =========================================================================================
#                                get_daily_quote
# =========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
# -----------------------------------------------------------------------------------------
def get_daily_quote(url):
    """
    This method gets the daily quote and author
    from brainyquote.com
    """
    html_soup = get_soup(url)
    dq_containers = html_soup.find_all('div', class_='clearfix')
    first_quote = dq_containers[0]
    # print(first_quote)

    # accessing the dq text
    dq = first_quote.a.text

    # accessing the dq author text
    author_containers = first_quote.find_all('a')
    author = author_containers[1].text

    return "{}\n\t-{}".format(dq, author)


# =========================================================================================
#                                  getHighLows
# =========================================================================================
# Author: Nichoas Ellis
# Init date:    11/07/18
# Last Updated: 11/27/18
# -----------------------------------------------------------------------------------------
def getHighLows(zipcode, dayNum):
    """
    returns array
    highLow[0] = high temperature
    highLow[1] = low  temperature
    """
    # Uses zipcode to get city name and state.
    zipCodeInfo = zipcodes.matching(zipcode)
    zipCodeInfo = zipCodeInfo[0]
    city = zipCodeInfo["city"].lower().title()
    state = zipCodeInfo["state"]

    # Get the data
    data = requests.get('https://weather.com/weather/tenday/l/' + city + '+' + state + '+' + zipcode + ':4:US')
    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    # Get data within a specific element
    data = []
    div = soup.find('div', {'class': 'temp'})
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    temp = data[dayNum][3].encode('ascii', 'ignore').decode('ascii')
    print(temp)
    highLow = [temp[0:len(temp)-2], temp[len(temp)-2:]]



    # If the high value is null '--' swap with N/A and reformat output
    if (highLow[0][:2] == '--'):
        #highLow[1] = highLow[0][2:]
        highLow[0] = '[N/A]'
        # If both are null
        if (highLow[1] == '--'):
            highLow[1] = '[N/A)]'
    # If the low value is null '--' swap with N/A and reformat output
    if (highLow[0][2:] == '--'):
        highLow[0] = highLow[0][:2]
        highLow[1] = '[N/A]'

    return highLow


# =========================================================================================
#                                  forecastStringBuilder
# =========================================================================================
# Author: Nichoas Ellis
# Init date:    11/15/18
# Last Updated: 11/27/18
# -----------------------------------------------------------------------------------------
def forecastStringBuilder(forecast, id):
    """
    id = 0 for current weather format
    id = 1 for current weekly  format
    id = 2 for furture weekly  format
    """

    if id == 0:
        forecastString = "The weather in {}, {} is {}.\nThe temperature is currently {} *F with a high of {} *F and a low of {} *F.\nThe wind speed is {} MPH.\n".format(
            forecast[0], forecast[1], forecast[3], str(forecast[2]), str(forecast[5]), str(forecast[6]),
            str(forecast[4]))
    if id == 1:
        forecastString = "The weather today is {} with a high of {} *F and a low of {}  *F.\n".format(forecast[3],
                                                                                                      str(forecast[5]),
                                                                                                      str(forecast[6]))
    if id == 2:
        forecastString = "The weather on {} will be {} with a high of {} *F and a low of {} *F.\n".format(forecast[7],
                                                                                                          forecast[3],
                                                                                                          str(forecast[
                                                                                                                  5]),
                                                                                                          str(forecast[
                                                                                                                  6]))

    return forecastString


# =========================================================================================
#                                  getForecastData
# =========================================================================================
# Author: Nichoas Ellis
# Init date:    11/13/18
# Last Updated: 11/27/18
# -----------------------------------------------------------------------------------------
def getForecastData(zipcode, response, dayNum, dayOfWeek):
    """
    Use "null" for dayOfWeek param
    unless using string format id = 2
    """
    # Uses zipcode to get city name and state.
    zipCodeInfo = zipcodes.matching(zipcode)
    zipCodeInfo = zipCodeInfo[0]

    # Store in easy to use variables
    city = zipCodeInfo["city"].lower().title()
    state = zipCodeInfo["state"]
    currentTemp = response["main"]["temp"]
    currentTemp = int(currentTemp)
    description = response["weather"][0]["description"]
    winds = response["wind"]["speed"]
    winds = int(winds)

    # Take current date's high's and lows
    highLow = getHighLows(zipcode, dayNum)
    high = highLow[0]
    low = highLow[1]

    # Forecast array
    forecast = [city, state, currentTemp, description, winds, high, low, dayOfWeek]
    return forecast


# =========================================================================================
#                                  getFiveDay
# =========================================================================================
# Author: Nichoas Ellis
# Init date:    11/13/18
# Last Updated: 11/15/18
# -----------------------------------------------------------------------------------------
def getFiveDay(zipcode):
    # Five Day Weather api url
    fivURL = "http://api.openweathermap.org/data/2.5/forecast?zip=" + zipcode + "&appid="
    fivURL += apiKey + "&units=imperial"

    # Get fivURL web request
    fivResponse = requests.get(fivURL).json()

    # ISO Weekday: 1 = Monday, ..., 7 = Sunday
    dateTimeObject = datetime.datetime.now()
    ISOday = dateTimeObject.isoweekday()

    nextFive = []
    # Get text format of the next five days
    for x in range(1, 5):
        # Increment
        ISOday = ISOday + 1
        index = ISOday % 7
        nextFive.append(calendar.day_name[index])

    # Gets forecast for next 5 days
    forecast1 = getForecastData(zipcode, fivResponse["list"][1], 1, "null")
    forecast2 = getForecastData(zipcode, fivResponse["list"][2], 2, nextFive[0])
    forecast3 = getForecastData(zipcode, fivResponse["list"][3], 3, nextFive[1])
    forecast4 = getForecastData(zipcode, fivResponse["list"][4], 4, nextFive[2])
    forecast5 = getForecastData(zipcode, fivResponse["list"][5], 5, nextFive[3])

    # Builds the forecast string
    forecast = "The forecast for " + forecast1[0] + ", " + forecast1[1]
    forecast += " for the next five days: \n" + forecastStringBuilder(forecast1, 1)
    forecast += forecastStringBuilder(forecast2, 2) + forecastStringBuilder(forecast3, 2)
    forecast += forecastStringBuilder(forecast4, 2) + forecastStringBuilder(forecast5, 2)

    return forecast


# =========================================================================================
#                                   getWeather
# =========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated: 11/15/18
# -----------------------------------------------------------------------------------------
def getWeather(zipcode):
    # OpenWeatherMap API current weather url
    curURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&appid="
    curURL += apiKey + "&units=imperial"

    # Get curURL web request
    curResponse = requests.get(curURL).json()

    # Builds the forecast string
    forecast = getForecastData(zipcode, curResponse, 1, "null")

    return forecastStringBuilder(forecast, 0)


# =========================================================================================
#                            tweetGreenvilleWeather
# =========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated:
# -----------------------------------------------------------------------------------------
def tweetGreenvilleWeather():
    # Greenville, NC 27858
    zipcode = "27858"

    # Builds the forecast string
    forecast = getWeather(zipcode)
    print(forecast)

    # Tweet the forecast
    api.update_status(status=forecast)
    database.addMessage("main.py", "tweets", "The weather was tweeted.  " + forecast)
    database.addMessage("main.py", "online", "Script main.py is still working.")

# =========================================================================================
#                                      main
# =========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated:
# -----------------------------------------------------------------------------------------
# Everyday at 8am tweet Greenville weather
schedule.every().day.at("13:00").do(tweetGreenvilleWeather)

#          DEBUG
# --------------------------
# Manually tweet
# tweetGreenvilleWeather()

# Manually print weather
print(getWeather("27858"))

# Manually print five day forecast
# print(getFiveDay("27858"))

# Manually print daily quote
# print(get_daily_quote(url))

# Manually print highLow
#print(getHighLows('27858', 1))

while True:
    schedule.run_pending()
    time.sleep(1)