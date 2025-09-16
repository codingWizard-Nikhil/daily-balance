# Daily Balance

A Python script that retrieves bank balances via Plaid and sends them via Twilio at a scheduled time every day.  
Currently a demo.

## How it works
- Connects to Plaid to fetch account balances.
- Sends the balances via Twilio using SMS or Whatsapp.

## Status
This is an early demo version. Future updates will:
- Move secrets to a .env file.
- Add scheduling via cloud functions.
- Improve error handling and logging.

## Author
Nikhil