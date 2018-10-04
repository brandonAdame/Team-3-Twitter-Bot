import requests #Python HTTP for Humans.

apiKey = "07a6ed1ad10a5c97fa9daa3c5babcaab"
#Zipcodes for testing
#####New York City 10001
#####Miami, Fl 33101
#####Greenville, NC 27834
#####Dallas, Tx 75001
#####Los Angeles, Ca 90001
zipCode = "27834"
apiURL = "http://api.openweathermap.org/data/2.5/weather?zip="+zipCode+"&appid="+apiKey+"&units=imperial"


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
print("The weather in " + location + " (" + coord + ") is " + description + ".  The temperature is currently " + str(currentTemp) + " *F with a high of " + str(high) + " *F and a low of " + str(low) + " *F.  The wind speed is " + str(winds) + " MPH.")
