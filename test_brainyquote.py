import unittest
from brainyquote import get_daily_quote
from requests import get
from bs4 import BeautifulSoup

class TestBrainyquote(unittest.TestCase):
    def test_get_daily_quote(self):
        # Test the daily quote value
        curr_quote = "Laughter is the sensation of feeling good all over and \
        showing it principally in one place\n\t-Josh Billings"
        self.assertEquals(curr_quote, get_daily_quote)
        