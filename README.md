# Team 3 Twitter Bot
A twitter bot that messages users the weather based on conditions that they specifies. The bot will also tweet daily at 8 a.m. the weather forecast for Greenville, N.C.

![image](https://img.shields.io/badge/completion-95%25-blue.svg)

![image](http://www.smallplanet.com/soapbox/wp-content/uploads/2018/06/22adb21cd5efbf3d4dde9a8ce8c188c3.jpg)

## Getting Started

1. Clone the repo `git clone git@github.com:ECU-CSCI-3030/Team-3-Twitter-Bot.git`

2. Install dependencies.

   ```
   pip install requests
   pip install feedparser
   pip install time
   pip install tweepy
   pip install schedule
   pip install zipcodes
   ```

3. Activate virtual environment: `source Team-3-Twitter-Bot/bin/activate`

4. To run a Python program, do `python [program-name].py`

5. To deactivate virtualenv, type this in your terminal `deactivate`



## Running Unit Tests

To run unit tests for do: `python -m unittest`
The following also works: `python -m unittest <module name>`



## Project Timeline

The project will be based on a weekly sprints. The project will be presented on December 5th at 8-10:30am.

**Weeks:**

1. Build weather module
2. Build database
3. Database testing
4. Build the direct messaging feature

- Build clothing suggestion module
- Build daily quote module
- Build word of the day module
- Build top news headline module
- Build shower thoughts module



## Built With

- [Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html) - Accessing the Twitter API.
- [Twitter Direct Message](https://developer.twitter.com/en/docs/direct-messages/api-features) - Provides access to endpoints to start conversations with a welcome message, publish messages with quick replies and media, and more.
- [OpenWeatherMap](https://openweathermap.org/api) - Pulls current weather data.
- [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) - The request interface of the Fetch API represents a resource request.
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Used for pulling data out of HTML and XML files.
- [virtulaenv](https://virtualenv.pypa.io/en/stable/) - Is a tool to create isolated Python environments.
- [zipcodes](https://pypi.org/project/zipcodes/) - A lightweight U.S. zip-code validation package for Python (2 and 3).
- [schedule](https://pypi.org/project/schedule/) - Python job scheduling for humans. 
- [time](https://docs.python.org/2/library/time.html) - This module provides various time-related functions.



## Project Contributers

- [Trevor](https://github.com/Downeyt16)

- [Nick](https://github.com/ellisn15)

- [Daniel](https://github.com/DanielLeeMeeks)

- [Jared](https://githib.com/phillipsjar12)

- [Brandon](https://github.com/brandonAdame)

