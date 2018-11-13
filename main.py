#=========================================================================================
#										 Imports
#=========================================================================================
import requests 	#Python HTTP for Humans.
import feedparser
import time
import tweepy 		#Twitter API
import zipcodes		#zipcodes database
import schedule		
import datetime
from requests import get
from bs4 import BeautifulSoup



#=========================================================================================
#										 API Keys
#=========================================================================================
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

#=========================================================================================
#                            		get_soup
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------
def get_soup(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup

#=========================================================================================
#                            get_len_quote_containers
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------

def get_len_quote_containers(url):
    html_soup = get_soup(url)

    # gets types of quotes available
    quote_containers = html_soup.find_all('h2', class_ = 'qotd-h2') 
    print(quote_containers)  # displays categories of quotes

    return len(quote_containers)


#=========================================================================================
#                                get_daily_quote
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 	9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------
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

    # print("{}\n\t-{}".format(dq, author))
    return "{}\n\t-{}".format(dq, author)

#=========================================================================================
#                                  forecastHelper
#=========================================================================================
# Author: Nichoas Ellis
# Init date: 	11/13/18
# Last Updated: 11/13/18
#-----------------------------------------------------------------------------------------
def forecastHelper(zipcode, response):
	# Uses zipcode to get city name and state.
	zipCodeInfo = zipcodes.matching(zipcode)
	zipCodeInfo = zipCodeInfo[0]

	# Store in easy to use variables
	currentTemp = response["main"]["temp"]
	city 		= zipCodeInfo["city"].lower().title()
	state 		= zipCodeInfo["state"]
	high 		= response["main"]["temp_max"]
	low 		= response["main"]["temp_min"]
	winds 		= response["wind"]["speed"]
	description = response["weather"][0]["description"]

	# Builds the forecast string
	forecast = "The weather in " + city + ", " + state + " is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH."
	# Send back forecast
	return forecast

#=========================================================================================
#                                  getFiveDay
#=========================================================================================
# Author: Nichoas Ellis
# Init date: 	11/13/18
# Last Updated: 11/13/18
#-----------------------------------------------------------------------------------------
def getFiveDay(zipcode):
	# Five Day Weather
	fivURL = "http://api.openweathermap.org/data/2.5/forecast?zip="+ zipcode + "&appid=" + apiKey + "&units=imperial"

	# Get fivURL web request
	fivResponse = requests.get(fivURL).json()



	# Call getHighLows
	day2 		= fivResponse["list"][2]
	forecast2 	= forecastHelper(zipcode, day2)
	#print(forecast1)

	day3		= fivResponse["list"][3]
	forecast3 	= forecastHelper(zipcode, day3)
	#print(forecast2)

	day4		= fivResponse["list"][4]
	forecast4 	= forecastHelper(zipcode, day4)
	#print(forecast3)

	day5		= fivResponse["list"][5]
	forecast5 	= forecastHelper(zipcode, day4)
	#print(forecast4)

	day6		= fivResponse["list"][6]
	forecast6	= forecastHelper(zipcode, day6)
	#print(forecast5)


	# Builds the forecast string
	forecast = "The forecast for the next five days: \n"+ forecast2 + forecast3 + forecast4 + forecast5 + forecast6
	# Send back forecast
	return forecast

#=========================================================================================
#                                   getWeather
#=========================================================================================
# Author: Nicholas Ellis
# Init date: 
# Last Updated: 11/13/18
#-----------------------------------------------------------------------------------------
def getWeather(zipcode):
	# OpenWeatherMap API current weather url
	curURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&appid=" + apiKey + "&units=imperial"
	# Get curURL web request
	curResponse = requests.get(curURL).json()
	# Builds the forecast string
	forecast	= forecastHelper(zipcode, curResponse)
	# Send back forecast
	return forecast


#=========================================================================================
#                                  directMessage
#=========================================================================================
# Author:
# Init date:
# Last Updated:
#-----------------------------------------------------------------------------------------
def directMessage():

	# See Team-3-Twitter-Bot/TwitterAPI_Test/test.py

	return 0

#=========================================================================================
#                            tweetGreenvilleWeather
#=========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated:
#-----------------------------------------------------------------------------------------
def tweetGreenvilleWeather():
	# Greenville, NC 27858
	zipcode = "27858"
	# Builds the forecast string
	forecast = getWeather(zipcode)
	print(forecast)
	# Tweet the forecast
	api.update_status(status=forecast)

#=========================================================================================
#										main
#=========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated:
#-----------------------------------------------------------------------------------------
# Everyday at 8am tweet Greenville weather
schedule.every().day.at("08:00").do(tweetGreenvilleWeather)


# Manually tweet
#tweetGreenvilleWeather()
# Manually print weather
#print(getWeather("27858"))

#getWeather("27858")
print(getFiveDay("27858"))

#print(get_daily_quote(url))

while True:
    schedule.run_pending()
    time.sleep(1)
