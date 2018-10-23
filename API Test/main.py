#=========================================================================================
#										 Imports
#=========================================================================================
import requests 	#Python HTTP for Humans.
import feedparser
import time
import tweepy 		#Twitter API
import zipcodes		#zipcodes database
import schedule		#


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
#								tweetGreenvilleWeather
#=========================================================================================
# 					Get weather for Greenville, NC 27858 and tweets it.
#-----------------------------------------------------------------------------------------
def tweetGreenvilleWeather():
	#Greenville, NC 27858
	zipCode = "27858"
	#Uses zipcode to get city name and state.
	zipCodeInfo = zipcodes.matching(zipCode)
	zipCodeInfo = zipCodeInfo[0]

	#OpenWeatherMap API url
	apiURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode + "&appid=" + apiKey + "&units=imperial"

	#Get web request
	response = requests.get(apiURL).json()

	#Store in easy to use variables
	currentTemp = response["main"]["temp"]
	location 	= zipCodeInfo["city"].lower().title() +", "+ zipCodeInfo["state"]	
	coord 		= str( response["coord"]["lon"] )+ ", " + str(response["coord"]["lat"])
	high 		= response["main"]["temp_max"]
	low 		= response["main"]["temp_min"]
	winds 		= response["wind"]["speed"]
	description = response["weather"][0]["description"]

	#Builds the forcast string
	forcast = "The weather in " + location + " is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH."

	#Print the forcast
	print("Coordinates: (" + coord + ")")
	print(forcast)
	#Tweet the forcast
	api.update_status(status=forcast)

#=========================================================================================
#										main
#=========================================================================================
#Everyday at 8am tweet Greenville weather
schedule.every().day.at("08:00").do(tweetGreenvilleWeather)

#Manually tweet
#tweetGreenvilleWeather()

while True:
    schedule.run_pending()
    time.sleep(1)
