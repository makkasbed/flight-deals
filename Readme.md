## Flights Deals

This project makes use of the following APIs:

- Tequila API [docs here](https://tequila.kiwi.com/portal/docs/tequila_api/search_api)
- Sheety API [docs here](https://sheety.co)
- Twilio's SMS API [docs here](https://twilio.com/sms/docs)

To build a cheap flight price comparator.

**data_manager.py** handles the Sheety API calls:

- Retrieving data 
- Updating data

**flight_search.py** handles:
- Locations retrieval i.e. City to IATA Code
- Prices Retrieval

**notification_manager.py** sends an SMS to users when the need arises

**flight_data.py** handles the formating of the JSON data from the flight search API