#=========================================================================================
#                                        Imports
#=========================================================================================
import requests             #Python HTTP for Humans.
import feedparser           #Parse RSS Feeds
from requests import get    #Send HTTP Requests. 
from bs4 import BeautifulSoup


#=========================================================================================
#                                  getWordOfDay
#=========================================================================================
# File:         getWordOfDay.py
# Author:       Nichoas Ellis
# Init date:    11/16/18
# Last Updated: 11/16/18
#-----------------------------------------------------------------------------------------
def getWordOfDay():
    # Get the data
    data = requests.get('https://www.merriam-webster.com/word-of-the-day')
    # Load data into bs4
    soup = BeautifulSoup(data.text, 'html.parser')
    
    # Get word using BeautifulSoup
    word = soup.find('div',{"class": "word-and-pronunciation"}).text.split("\n")[1].title()
    # Get definition using BeautifulSoup
    definition = soup.find('div',{"class": "wod-definition-container"}).text.split("\n")[2]
    # Format output string
    wod = word + definition
    
    # Debug
    #print(wod)

    return wod
