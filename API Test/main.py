#=========================================================================================
#											Imports
#=========================================================================================
import requests 	#Python HTTP for Humans.
import feedparser
import time
import tweepy
#Yahoo app
from urllib.request import urlopen
import urllib
import json


#=========================================================================================
#											Keys
#=========================================================================================
#OpenWeatherMap Key
apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

#Yahoo Keys
yahoo_consumer_key = "dj0yJmk9OVE2YmlWTzNUZUlnJmQ9WVdrOVpFMVhja2hQTlRBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD0wNQ--"
yahoo_consumer_key_secret = "ebfc93894a327ac06a60d075905b03b9a139a3ff"

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
#									Implementation
#=========================================================================================
# 					Get weather for Greenville,NC 27858 and tweet it.
#-----------------------------------------------------------------------------------------

# Yahoo!'s limit on the number of days they will forecast
DAYS_LIMIT = 2
WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
METRIC_PARAMETER = '&u=c'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def get_weather(location_code, options):
    """
    Fetches weather report from Yahoo!
    :Parameters:
    -`location_code`: A five digit US zip code.
    -`days`: number of days to obtain forecasts
    :Returns:
    -`weather_data`: a dictionary of weather data
    """

    # Get the correct weather url.
    url = WEATHER_URL % location_code

    if options.metric:
        url = url + METRIC_PARAMETER

    # Parse the XML feed.
    try:
        dom = parse(urllib.urlopen(url))
    except Exception:
        return None

    # Get the units of the current feed.
    yunits = dom.getElementsByTagNameNS(WEATHER_NS, 'units')[0]

    # Get the location of the specified location code.
    ylocation = dom.getElementsByTagNameNS(WEATHER_NS, 'location')[0]

    # Get the current conditions.
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]

    # Hold the forecast in a hash.
    forecasts = []

    # Walk the DOM in order to find the forecast nodes.
    for i, node in enumerate(dom.getElementsByTagNameNS(WEATHER_NS, 'forecast')):

        # Stop if the number of obtained forecasts equals the number of requested days
        if i >= options.forecast:
            break
        else:
            # Insert the forecast into the forcast dictionary.
            forecasts.append({
                'date': node.getAttribute('date'),
                'low': node.getAttribute('low'),
                'high': node.getAttribute('high'),
                'condition': node.getAttribute('text')
            })

    # Return a dictionary of the weather that we just parsed.
    weather_data = {
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'forecasts': forecasts,
        'units': yunits.getAttribute('temperature'),
        'city': ylocation.getAttribute('city'),
        'region': ylocation.getAttribute('region'),
    }

    return weather_data

def main(argv):
	print(argv)
	# Get the weather.
	weather = get_weather(args.location_code, args)

	print(weather)
	#api.update_status(status="The weather in " + location + " (" + coord + ") is " + description + ".\nThe temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.\nThe wind speed is " + str(winds) + " MPH.")

