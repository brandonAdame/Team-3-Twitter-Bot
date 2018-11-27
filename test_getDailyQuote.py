import unittest
from getDailyQuote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_brainyquote.py

class TestgetDailyQuote(unittest.TestCase):
    def test_get_daily_quote(self):
        # curr_quote = "Who covets more is evermore a slave.\n-Robert Herrick"
        s = get_daily_quote()
        self.assertEqual(s, "Who covets more is evermore a slave.\n-Robert Herrick")

if __name__ == '__main__':
    unittest.main