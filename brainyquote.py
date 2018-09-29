"""
File: brainyquote.py
Author: Brandon Adame Gachuz
Init date: 9/28/2018

This file is intended to be used to get the quote of the day
from brainyquote.com

Since brainyquote does not provide an API, I used a couple of
powerful libraries to scrape the daily quote from their website.
"""
from requests import get
from bs4 import BeautifulSoup

url = "https://www.brainyquote.com/quote_of_the_day"

def get_soup(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup

def get_len_quote_containers(url):
    html_soup = get_soup(url)

    # gets types of quotes available
    quote_containers = html_soup.find_all('h2', class_ = 'qotd-h2') 
    print(quote_containers)  # displays categories of quotes

    return len(quote_containers)

# print(get_len_quote_containers())

def get_daily_quote(url):
    """
    This method gets the daily quote from brainyquote.com
    along with the author
    """
    html_soup = get_soup(url)
    dq_containers = html_soup.find_all('div', class_='clearfix')
    first_quote = dq_containers[0]
    # print(first_quote)

    # accessing the dq text
    dq = first_quote.a.text

    # accessing the dq author text
    author = first_quote.find('a', class_="bq-aut qa_107273 oncl_a").text
    print("{}\n\t-{}".format(dq, author))


    

get_daily_quote(url)