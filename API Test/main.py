import requests #Python HTTP for Humans.
import feedparser
import time
import tweepy

apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

#Twitter keys
#@CSCIteam3
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_token = "1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_token_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"

#Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Raleigh, NC 27834
zipCode = "27858"
apiURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode + "&appid=" + apiKey + "&units=imperial"

#Get web request
response = requests.get(apiURL).json()

#Store in easy to use variables
currentTemp = response["main"]["temp"]
location = response["name"]
coord = str( response["coord"]["lon"] )+ ", " + str(response["coord"]["lat"])
high = response["main"]["temp_max"]
low = response["main"]["temp_min"]
winds = response["wind"]["speed"]
description = response["weather"][0]["description"]

#Print the forcast
#message = "The weather in " + location + " (" + coord + ") is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH.")

api.update_status(status="The weather in " + location + " (" + coord + ") is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH.")