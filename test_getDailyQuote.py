import unittest
from requests import get
from bs4 import BeautifulSoup

class TestgetDailyQuote(unittest.TestCase):
	def test_get_daily_quote(self):
	
	curr_quote = "One that would have the fruit must climb the tree\n\t-Thomas Fuller"
	self.assertEquals(curr_quote, get_daily_quote)