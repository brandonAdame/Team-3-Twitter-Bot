"""
File: daily-quote.py
Author: Brandon Adame Gachuz
Init date: 9/29/2018

This file will likely be removed
"""
from requests import get
import json


# link to random quote 
url = "http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"

# getting response
response = get(url)

# parsing through text
rlen = len(response.text)
response = response.text[1:rlen-1]
# print(response)

# converting from JSON to Python dict
ans = json.loads(response)
author = ans['title']
quote = ans['content']
print(quote)


