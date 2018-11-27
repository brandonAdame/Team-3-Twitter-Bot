import unittest
from getDailyQuote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_getDailyQuote.py

class TestgetDailyQuote(unittest.TestCase):
    # Test 1 (s = manual typed daily quote)
    def test_get_daily_quote(self):
        s = get_daily_quote()
        self.assertEqual(s, "Who covets more is evermore a slave.\n-Robert Herrick")
    #Test 1: passed
        
    # Test 2 (t != manual typed daily quote)
    def test_get_daily_quote_fail(self):
    	t = get_daily_quote()
    	self.assertNotEqual(t, "ho covets more is evermore a slave.\n-Robert Herrick")    
    # Test 2: passed	
if __name__ == '__main__':
    unittest.main