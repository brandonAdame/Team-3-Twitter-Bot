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


url = "https://www.brainyquote.com/quote_of_the_day"

#=========================================================================================
#                            		get_soup
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 9/28/2018
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
# Init date: 9/28/2018
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
# Init date: 9/28/2018
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
#                                  getHighLows
#=========================================================================================
# Author: Nichoas Ellis
# Init date:
# Last Updated:
#-----------------------------------------------------------------------------------------
def getHighLows(city, state, zipcode):

    # Get the data
    data = requests.get('https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US')
    print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US")

    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    # Get data within a specific element
    data = []
    div = soup.find('div', {'class': 'temp'})
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    return (data)


#=========================================================================================
#                                   getWeather
#=========================================================================================
# Author: Nicholas Ellis
# Init date: 
# Last Updated: 
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

    highLow = getHighLows(city, state, zipcode)[1][3]
    high = highLow.split("°")[0]
    #print(high)
    low = highLow.split("°")[1]
    #print(low)

    # Builds the forecast string
    forecast = "The weather in " + city + ", " + state + " is " + description + ".\nThe temperature is currently " + str(currentTemp) + " °F with a high of " + str(high) + " °F and a low of " + str(low) + " °F.\nThe wind speed is " + str(winds) + " MPH."
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
    # Gets the forecast
    forecast = getWeather(zipcode)
    print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] " + forecast)
    # Tweet the forecast
    api.update_status(status=forecast)

#=========================================================================================
#										main
#=========================================================================================
# Author: Nicholas Ellis
# Init date:
# Last Updated:
#-----------------------------------------------------------------------------------------
# Everyday at 8am (13:00 GMT) tweet Greenville weather
schedule.every().day.at("13:00").do(tweetGreenvilleWeather)


# Manually tweet
#tweetGreenvilleWeather()
# Manually print weather
#print(getWeather("27858"))

print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] " + get_daily_quote(url))

#tweetGreenvilleWeather()

#print (getHighLows("Greenville", "NC", "27858")[1][3])

#getHighLows("Greenville", "NC", "27858")

while True:
    schedule.run_pending()
    time.sleep(1)
