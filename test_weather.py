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

This module tests the reqirement for: weather
'''

class Testweather(unittest.TestCase):
    def test_get_high_lows(self):
        pass

    def test_get_weather(self):
        """
        The 'weather' variable is manually written each day to match with getWeather() return value
        """
        curr_forecast = getWeather('27889')
        weather = "The weather in Washington, NC is clear sky. The temperature is currently 47.14 *F. Max: 49 / Min: 28"
        self.assertEqual(weather, getWeather('27889'))
        self.assertNotEqual("This is a weather forecast", curr_forecast)


if __name__ == '__main__':
    unittest.main