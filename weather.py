# -*- coding: utf-8 -*-

#=========================================================================================
#                                    Imports
#=========================================================================================
import requests     #Python HTTP for Humans.
import feedparser   #Parse RSS Feeds
import time         #Time and Converting.
import tweepy       #Twitter API
import zipcodes     #zipcodes database
import schedule     #API for Schedulng jobs.
import datetime     #Manipulating Dates
from datetime import date
import calendar
from requests import get #Send HTTP Requests. 
from bs4 import BeautifulSoup

#=========================================================================================
#                                    API Keys
#=========================================================================================
#OpenWeatherMap Key
apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

#=========================================================================================
#                                  getHighLows
#=========================================================================================
# Author: Nichoas Ellis
# Init date:    11/07/18
# Last Updated: 11/27/18
#-----------------------------------------------------------------------------------------
def getHighLows(zipcode, dayNum):
    """
    returns array 
    highLow[0] = high temperature
    highLow[1] = low  temperature
    """
    # Uses zipcode to get city name and state.
    zipCodeInfo = zipcodes.matching(zipcode)
    zipCodeInfo = zipCodeInfo[0]
    city        = zipCodeInfo["city"].lower().title()
    state       = zipCodeInfo["state"]

    # Get the data
    data = requests.get('https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US')
    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    # Get data within a specific element
    data = []
    div = soup.find('div', {'class': 'temp'})
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)
    highLow = data[dayNum][3].split("°")
    
    # If the high value is null '--' swap with N/A and reformat output
    if(highLow[0][:2] == '--'):
        highLow[1] = highLow[0][2:]
        highLow[0] = '[N/A]'
        # If both are null
        if(highLow[1] == '--'):
            highLow[1] = '[N/A)]'
    # If the low value is null '--' swap with N/A and reformat output
    if(highLow[0][2:] == '--'):
        highLow[0] = highLow[0][:2]
        highLow[1] = '[N/A]' 
   
    #return (data)
    return highLow

#=========================================================================================
#                                  forecastStringBuilder
#=========================================================================================
# Author: Nichoas Ellis
# Init date:    11/15/18
# Last Updated: 11/27/18
#-----------------------------------------------------------------------------------------
def forecastStringBuilder(forecast, id):
    """
    id = 0 for current weather format
    id = 1 for current weekly  format
    id = 2 for furture weekly  format
    """

    if id == 0:
        forecastString = "The weather in {}, {} is {}.\nThe temperature is currently {} *F with a high of {} *F and a low of {} *F.\nThe wind speed is {} MPH.\n".format(forecast[0], forecast[1], forecast[3], str(forecast[2]), str(forecast[5]), str(forecast[6]), str(forecast[4])) 
    if id == 1:
        forecastString = "The weather today is {} with a high of {} *F and a low of {}  *F.\n".format(forecast[3], str(forecast[5]), str(forecast[6]))
    if id == 2:
        forecastString = "The weather on {} will be {} with a high of {} *F and a low of {} *F.\n".format(forecast[7], forecast[3], str(forecast[5]), str(forecast[6]))
    return forecastString


#=========================================================================================
#                                  getForecastData
#=========================================================================================
# Author: Nichoas Ellis
# Init date:    11/13/18
# Last Updated: 11/27/18
#-----------------------------------------------------------------------------------------
def getForecastData(zipcode, response, dayNum, dayOfWeek):
    """
    Use "null" for dayOfWeek param 
    unless using string format id = 2
    """
    # Uses zipcode to get city name and state.
    zipCodeInfo = zipcodes.matching(zipcode)
    zipCodeInfo = zipCodeInfo[0]

    # Store in easy to use variables
    city        = zipCodeInfo["city"].lower().title()
    state       = zipCodeInfo["state"]
    currentTemp = response["main"]["temp"]
    currentTemp = int(currentTemp)
    description = response["weather"][0]["description"]
    winds       = response["wind"]["speed"]
    winds       = int(winds)

    # Take current date's high's and lows
    highLow     = getHighLows(zipcode, dayNum)
    high        = highLow[0]
    low         = highLow[1]

    # Forecast array
    forecast = [city, state, currentTemp, description, winds, high, low, dayOfWeek]
    return forecast


#=========================================================================================
#                                  getFiveDay
#=========================================================================================
# Author: Nichoas Ellis
# Init date:    11/13/18
# Last Updated: 11/15/18
#-----------------------------------------------------------------------------------------
def getFiveDay(zipcode):
    # Five Day Weather api url
    fivURL  = "http://api.openweathermap.org/data/2.5/forecast?zip="+ zipcode + "&appid=" 
    fivURL += apiKey + "&units=imperial"
    
    # Get fivURL web request
    fivResponse = requests.get(fivURL).json()

    #ISO Weekday: 1 = Monday, ..., 7 = Sunday
    dateTimeObject = datetime.datetime.now()
    ISOday = dateTimeObject.isoweekday() 

    nextFive = []
    # Get text format of the next five days
    for x in range(1, 5):
        # Increment 
        ISOday = ISOday + 1
        index  = ISOday % 7
        nextFive.append(calendar.day_name[index])

    # Gets forecast for next 5 days
    forecast1   = getForecastData(zipcode, fivResponse["list"][1], 1, "null")
    forecast2   = getForecastData(zipcode, fivResponse["list"][2], 2, nextFive[0])
    forecast3   = getForecastData(zipcode, fivResponse["list"][3], 3, nextFive[1])
    forecast4   = getForecastData(zipcode, fivResponse["list"][4], 4, nextFive[2])
    forecast5   = getForecastData(zipcode, fivResponse["list"][5], 5, nextFive[3])

    # Builds the forecast string
    forecast  = "The forecast for "+ forecast1[0] + ", " + forecast1[1]
    forecast += " for the next five days: \n"+ forecastStringBuilder(forecast1, 1)
    forecast += forecastStringBuilder(forecast2, 2) + forecastStringBuilder(forecast3, 2) 
    forecast += forecastStringBuilder(forecast4, 2) + forecastStringBuilder(forecast5, 2)
    
    # Send back forecast
    return forecast


#=========================================================================================
#                                   getWeather
#=========================================================================================
# Author: Nicholas Ellis
# Init date: 
# Last Updated: 11/15/18
#-----------------------------------------------------------------------------------------
def getWeather(zipcode):
    # OpenWeatherMap API current weather url
    curURL  = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&appid=" 
    curURL += apiKey + "&units=imperial"
    
    # Get curURL web request
    curResponse = requests.get(curURL).json()

    # Builds the forecast string
    forecast = getForecastData(zipcode, curResponse, 1, "null")

    # Send back forecast
    return forecastStringBuilder(forecast, 0)


#=========================================================================================
#                                    main
#=========================================================================================
if __name__ == '__main__':
    zipcode = '27858'
    # Debug
    #print(getHighLows(zipcode, 1))
    print(getWeather(zipcode))
    #print(getFiveDay(zipcode))
