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

### Prerequisites
- A **SHEET_URL** that connects to your Google Sheets Project in Sheety.


- An **F_API_KEY** that is the API KEY from Tequila

- A **FLIGHT_URL** that links to the Tequila Base URL

- An **SID** from Twilio

- An **SKEY** from Twilio

- An **ANUM** which is a phone number from Twilio.

These parameters can be set as environment variables using the **export** command.

Example:

``
export SID=a2v35bh6ji89ue
``