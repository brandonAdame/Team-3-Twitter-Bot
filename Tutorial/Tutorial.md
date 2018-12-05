# Team 3 Twitter Bot Tutorial
A twitter bot that messages users the weather based on conditions that they specifies. The bot will also tweet daily at 8 am EST the weather forecast for Greenville, N.C.

## Getting Started

1. Open web browser or Twitter app and navigate to: 

   - https://twitter.com/csci3030team3
   - [@csci3030team3](https://twitter.com/csci3030team3)

2. Follow for our daily Greenville, NC weather forecast. Tweeted at 8am EST

3. Turn on notifications by selecting the bell icon. This will notify you imeadiatly with our daily forecast tweet.

4. DM the bot to recive a message for your local weather at the time you need it using the commands below.  Also sign up for daily quotes and the word of the day or a reminder.

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
  !add localWeather [zipCode] [time to send weather everyday, HH:MM:SS, optional]
  !add dailyQuote
  !add word
  !add remindMe [date, YYYY-MM-DD] [time, HH:MM:SS] [message]
```

Message Example:

!help command:

```
User: !help

Bot: '!info'
     See a list of the events you are signed up for.
'!unsub [eventID]'
     Unsubscribe from an event.
'!unsubAll'
     Unsubscribe from all events
'!time'
     All times are in GTM London (5 hours before EST New York) See the server time by sending .
'!add [eventType] [parameters1] [parameters2]...'
     Add a new event.

Bot: Types of events:
     LOCAL WEATHER:
          '!add localWeather [zipCode] [time to send weather, formatted HH:MM:SS (24 hour time).  optional]'
          Sends the local weather at the time you want (defalt 8AM).
     DAILY QUOTE:
          '!add dailyQuote'
          Sends a daily quote every morning at 7AM.
     DAILY STOCK*:
          '!add dailyStocks [stock symbol]'
          Send the value of a stock everyday after the stock market cloeses (5:30PM).
     WORD OF THE DAY:
          '!add word'
          Sends a daily word every morning at 9AM.
     REMIND ME:
          '!add remindMe' [data, formatted YYYY MM DD] [time, formatted HH:MM:SS] [message]
     Send you a reminder on the date and time you pick.
```

!add [eventType]

```
User: !add dailyquote
User: !add word

Bot: You will receive a DM of a word everyday at 9 AM.
Bot: You will receive a DM of a quote everyday at 7 AM.
```

