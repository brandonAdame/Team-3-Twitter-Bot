#=========================================================================================
#                                    Imports
#=========================================================================================
import requests 	#Python HTTP for Humans.
import zipcodes		#zipcodes database.
import datetime		#Manipulating Dates
from bs4 import BeautifulSoup	#Parsing HTML/XML files.

#=========================================================================================
#                                    API Keys
#=========================================================================================
#OpenWeatherMap Key
apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"

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
    # print("[" + str(datetime.datetime.now()) +", API Test/NWSPublicAlerts_twitter.py] https://weather.com/weather/tenday/l/'+city+'+'+state+'+'+zipcode+':4:US")

    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')

    # Get data within a specific element
    data = []
    div = soup.find('div', {'class': 'temp'})
    for tr in soup.find_all('tr'):
        values = [td.text for td in tr.find_all('td')]
        data.append(values)

    # print(data)
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

    highLow = getHighLows(city, state, zipcode)[1][3].encode('ascii', 'ignore').decode('ascii')
    ##print(chr(176))
    high = highLow[0:len(highLow)-2]
    #print(high)
    low = highLow[len(highLow)-2:len(highLow)]
    #print(low)

    # Builds the forecast string
    forecast = "The weather in {}, {} is {}. The temperature is currently {} *F. Max: {} / Min: {}".format(city, 
    state, description, str(currentTemp), str(high), str(low))
    # forecast = "The weather in " + city + ", " + state + " is " + description + ".  The temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.  The wind speed is " + str(winds) + " MPH."
    # Send back forecast
    # print(forecast)
    return forecast

if __name__ == '__main__':
    getWeather('27889')