import unittest
from getDailyQuote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_getDailyQuote.py

#NOTE: The quote of the day needs to be manually pulled from "https://www.brainyquote.com/quote_of_the_day"
actualQuote = get_daily_quote()
class TestgetDailyQuote(unittest.TestCase):

    # Test 1 (s = manual typed daily quote)
    def test_get_daily_quote(self):
        self.assertEqual(actualQuote, "The great advantage about telling the truth is that nobody ever believes it.\n-Dorothy L. Sayers")
    #Test 1: passed
        
    # Test 2 (actualQuote != manual typed daily quote)
    # This test is designed to compare the actual daily quote with an "unequal" quote
    def test_get_daily_quote_fail(self):
    	self.assertNotEqual(actualQuote, "ho covets more is evermore a slave.\n-Robert Herrick")    
    # Test 2: passed	
    
if __name__ == '__main__':
    unittest.main