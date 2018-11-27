import unittest
from getDailyQuote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

# How to run tests: python -m unittest test_getDailyQuote.py

class TestgetDailyQuote(unittest.TestCase):
<<<<<<< HEAD
	def test_get_daily_quote(self):
		# curr_quote = "Who covets more is evermore a slave.\n-Robert Herrick"
		s = get_daily_quote()
		self.assertEqual(s, "Who covets more is evermore a slave.\n-Robert Herrick")
=======
    def test_get_daily_quote(self):
        # curr_quote = "Who covets more is evermore a slave.\n-Robert Herrick"
        s = get_daily_quote()
        self.assertEqual(s, "Who covets more is evermore a slave.\n-Robert Herrick")
>>>>>>> 6076478842176aa605f8b59fa9dc9446dbc2321a

if __name__ == '__main__':
    unittest.main