import unittest
from getDailyQuote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_brainyquote.py

class TestgetDailyQuote(unittest.TestCase):
	def test_get_daily_quote(self):
		curr_quote = "One that would have the fruit must climb the tree\n-Thomas Fuller"
		self.assertEquals(curr_quote, get_daily_quote)