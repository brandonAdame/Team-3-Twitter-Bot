import tweepy
import pyowm

# credentials
consumer_key = "ThbfGVBrpRwMKu9FVgR6HjA1m"
consumer_secret = "lGyzD69pQGupB4lTG3jWG8rszYmVN4CGjFPYGUBTr1EhKdiBxh"
access_token = 	"1039183691510165505-IkoKTm8MopQ3PzYVmEgU2NdGmognPL"
access_token_secret = "jwWe8WqunRcmqKWgvYyDuUjkyotgfUddeLKcTHYz40ktP"
owm_key = "49c2f7c5be853b9d60beee601f36a2d5"

# login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# autheticating
api = tweepy.API(auth)
owm = pyowm.OWM(owm_key)

print('authentication successful')

observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w)

"""
# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
"""

phrase = 'greetings from Greenville!'
api.update_status(phrase)