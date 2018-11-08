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
import bs4
from requests import get
import json


#=========================================================================================
#										 API Keys
#=========================================================================================
#OpenWeatherMap Key
apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

#Twitter keys (@CSCIteam3)
twitter_consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
twitter_consumer_key_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
twitter_access_key = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
twitter_access_key_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

#Tweepy authentication
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_key_secret)
auth.set_access_token(twitter_access_key, twitter_access_key_secret)
api = tweepy.API(auth)


#=========================================================================================
#                                  getHighLows
#=========================================================================================
def getHighLows(city, state, zipcode):

	# Get the data
	data = requests.get('https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US')
	print('https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US')

	# Load data into bs4
	soup = BeautifulSoup(data.text, 'html.parser')

	# Get data within a specific element
	data = []
	div = soup.find('div', {'class': 'temp'})
	for tr in soup.find_all('tr'):
		values = [td.text for td in tr.find_all('td')]
		data.append(values)

	print(data)



#=========================================================================================
#                                   getWeather
#=========================================================================================
#                        Param zipcode must be a string
#-----------------------------------------------------------------------------------------
def getWeather(zipcode):
	# Uses zipcode to get city name and state.
	zipCodeInfo = zipcodes.matching(zipcode)
	zipCodeInfo = zipCodeInfo[0]

	# OpenWeatherMap API current weather url
	curURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipcode + "&appid=" + apiKey + "&units=imperial"


	# Get curURL web request
	curResponse = requests.get(curURL).json()

	# Store in easy to use variables
	currentTemp = curResponse["main"]["temp"]
	city 		= zipCodeInfo["city"].lower().title()
	state 		= zipCodeInfo["state"]

	# Call getHighLows
	#high 		= curResponse["main"]["temp_max"]
	#low 		= curResponse["main"]["temp_min"]

	winds 		= curResponse["wind"]["speed"]
	description = curResponse["weather"][0]["description"]

	print(high)
	print(low)

	# Builds the forecast string
	forecast = "The weather in " + city + ", " + state + " is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH."
	# Send back forecast
	return forecast


#=========================================================================================
#                                  directMessage
#=========================================================================================
def directMessage():

	# See Team-3-Twitter-Bot/TwitterAPI_Test/test.py

	return 0

#=========================================================================================
#                            tweetGreenvilleWeather
#=========================================================================================
#                Get weather for Greenville, NC 27858 and tweets it.
#-----------------------------------------------------------------------------------------
def tweetGreenvilleWeather():
	# Greenville, NC 27858
	zipcode = "27858"
	# Gets the forecast
	forecast = getWeather(zipcode)
	print(forecast)
	# Tweet the forecast
	api.update_status(status=forecast)

#=========================================================================================
#										main
#=========================================================================================
# Everyday at 8am tweet Greenville weather
schedule.every().day.at("08:00").do(tweetGreenvilleWeather)

# Manually tweet
#tweetGreenvilleWeather()
# Manually print weather
#print(getWeather("27858"))

print(dailyQuote)

#getHighLows("Greenville", "NC", "27858")

while True:
    schedule.run_pending()
    time.sleep(1)
