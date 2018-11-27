#=========================================================================================
#										 Imports
#=========================================================================================
from requests import get 	#Send HTTP Requests.
from bs4 import BeautifulSoup	#Parsing HTML/XML files.

url = "https://www.brainyquote.com/quote_of_the_day"

#=========================================================================================
#                            		get_soup
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------
def get_soup(url):
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup

#=========================================================================================
#                            get_len_quote_containers
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------

def get_len_quote_containers(url):
    html_soup = get_soup(url)

    # gets types of quotes available
    quote_containers = html_soup.find_all('h2', class_ = 'qotd-h2')
    print(quote_containers)  # displays categories of quotes

    return len(quote_containers)

#=========================================================================================
#                                get_daily_quote
#=========================================================================================
# File: brainyquote.py
# Author: Brandon Adame Gachuz
# Init date: 9/28/2018
# Last Updated: 9/29/2018
#-----------------------------------------------------------------------------------------
def get_daily_quote():
    """
    This method gets the daily quote and author
    from brainyquote.com
    """
    html_soup = get_soup(url)
    dq_containers = html_soup.find_all('div', class_='clearfix')
    first_quote = dq_containers[0]
    # print(first_quote)

    # accessing the dq text
    dq = first_quote.a.text

    # accessing the dq author text
    author_containers = first_quote.find_all('a')
    author = author_containers[1].text

    # print("{}\n\t-{}".format(dq, author))
    return "{}\n-{}".format(dq, author)