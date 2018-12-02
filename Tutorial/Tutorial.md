# Team 3 Twitter Bot Tutorial
A twitter bot that messages users the weather based on conditions that they specifies. The bot will also tweet daily at 8 am EST the weather forecast for Greenville, N.C.

## Getting Started

1. Open web browser or Twitter app and navigate to: 

   - https://twitter.com/csci3030team3
   - [@csci3030team3](https://twitter.com/csci3030team3)

   ==[picture]==

2. Follow for our daily Greenville, NC weather forecast. Tweeted at 8am EST

   ==[picture]==

3. Turn on notifications by selecting the bell icon. This will notify you imeadiatly with our daily forecast tweet.

   ==[picture]==

## Direct Message Commands

General Commnads:

```
!help               - Returns a list of commands available to the user
!info               - Returns a list of events the user
!info [eventID]     - Returns information about an event
!unsub [eventID]    - Unsubscribes a user from an event
!unsubAll           - Unsubscribes a user from all events
!time               - Responds with the server time (GMT)
```

Event Commands:

```
!add [eventType] [parameters1] [parameters2] [parameters3]...
  !add localWeather [zipCode] [time to send weather, optional]
  !add dailyQuote
  !add word
  !add dailyStocks [stock symbol]
```

Message Example:

```
User: !help

Bot: NOTE: This Twitter bot is not finished and may be unstable.  Follow @csci3030team3 to be notifyed when it is ready.
Bot: See a list of the events you are signed up for by sending '!info'
Bot: Unsubscribe from an event by sending '!unsub [eventID]' or unsubscribe from all events by sending '!unsubAll'
Bot: Add a new event by sending '!add [eventType] [parameters1] [parameters2]...'
Bot: Types of events:
Bot: LOCAL WEATHER: Sends the local weather at the time you want (defalt 8AM).  '!add localWeather [zipCode] [time to send weather, formatted HH:MM:SS (24 hour time).  optional]'
Bot: DAILY QUOTE*: Sends a daily quote every morning at 7AM.  '!add dailyQuote'
Bot: DAILY STOCK: Send the value of a stock everyday after the stock market cloeses (5:30PM).  '!add dailyStocks [stock symbol]'
Bot: WORD OF THE DAY: Sends a daily word every morning at 9AM.  '!add word'
```

