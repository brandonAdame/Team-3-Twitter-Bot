import unittest
import requests 	
import zipcodes		
import datetime		
from bs4 import BeautifulSoup
from weather import getHighLows, getWeather

'''
How to run: 
    1. Make sure virtual environment in active: source Team-3-Twitter-Bot/bin/activate
    2. Run the following command in bash: python -m unittest test_weather.py

This module tests the reqirement for: weather.py
'''

# Gobal variable
zipcode = '27858'

class Testweather(unittest.TestCase):
    def test_get_high_lows(self):
        """
        The 'highlow' variable is manually written each instance of running to match 
            with getHighLows() return value
        """
        curr_highLow = getHighLows(zipcode, 1)
        highLow = ['[N/A]', '28', '']
        
        self.assertEqual(highLow, getHighLows(zipcode, 1))
        self.assertNotEqual([''], curr_highLow)



    def test_getForecastData(self):
        """
        The 'fivDay' variable is manually written each instance of running to match 
            with getHighLows() return value
        """

        curr_fivDay = getFiveDay(zipcode)
        fivDay = "The forecast for Greenville, NC for the next five days: \n"
        fivDay += "The weather today is clear sky with a high of [N/A] *F and a low of 28  *F.\n"
        fivDay += "The weather on Thursday will be clear sky with a high of 44 *F and a low of 26 *F.\n"
        fivDay += "The weather on Friday will be clear sky with a high of 50 *F and a low of 35 *F.\n"
        fivDay += "The weather on Saturday will be clear sky with a high of 62 *F and a low of 46 *F.\n"
        fivDay += "The weather on Sunday will be clear sky with a high of 68 *F and a low of 57 *F.\n"

        self.assertEqual(fivDay, getFiveDay(zipcode))
        self.assertNotEqual("The forecast for the next five days", curr_fivDay)



    def test_get_weather(self):
        """
        The 'weather' variable is manually written each day to match with 
            getWeather() return value
        """
        curr_forecast = getWeather(zipcode)
        weather = "The weather in Greenville, NC is clear sky.\nThe temperature is currently 49 *F with a high of 50 *F and a low of 28 *F.\nThe wind speed is 6 MPH.\n"
        
        self.assertEqual(weather, getWeather(zipcode))
        self.assertNotEqual("The weather today is", curr_forecast)


if __name__ == '__main__':
    unittest.main
