import unittest
from brainyquote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_brainyquote.py

class TestBrainyquote(unittest.TestCase):
    def testGetDailyQuote(self):
        s = get_daily_quote
        curr_quote = "Who covets more is evermore a slave.\n-Robert Herrick"
        self.assertEqual(curr_quote, s)

if __name__ == '__main__':
    unittest.main
        