# Daily-Balance

A serverless banking notification system that sends daily account balance updates via WhatsApp. Built with AWS Lambda, Plaid API, and Twilio.

## Features

- **Serverless Architecture**: Runs on AWS Lambda - no server maintenance required
- **Automated Scheduling**: EventBridge triggers daily notifications
- **Secure Credential Management**: Uses AWS environment variables for API keys
- **Real-time Banking Data**: Integrates with Plaid API for account balances
- **WhatsApp Notifications**: Sends balance updates via Twilio

## Tech Stack

- **Backend**: Python 3.13
- **Cloud Platform**: AWS Lambda
- **Scheduling**: AWS EventBridge (CloudWatch Events)
- **APIs**: 
  - Plaid API (Banking data)
  - Twilio API (WhatsApp messaging)
- **Deployment**: Packaged with dependencies as Lambda deployment package

## Architecture
```
EventBridge (Daily Trigger) → Lambda Function → Plaid API → Twilio API → WhatsApp
```

## Local Development

1. Clone the repository
```bash
git clone https://github.com/codingWizard-Nikhil/daily-balance.git
cd daily-balance
```

2. Create virtual environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Create `config.py` with your credentials
```python
# Plaid credentials
plaid_id = "your_plaid_client_id"
plaid_secret = "your_plaid_secret"

# Twilio credentials
account_sid = "your_twilio_account_sid"
auth_token = "your_twilio_auth_token"
twilio_number = "whatsapp:+14155238886"
user_phone = "whatsapp:+1234567890"
```

4. Run locally
```bash
python3 src/main.py
```

## AWS Lambda Deployment

### Prerequisites
- AWS Account
- AWS CLI configured (optional)

### Deployment Steps

1. **Create deployment package**
```bash
mkdir lambda_package
cd lambda_package
pip install --target . plaid-python twilio
cp ../src/*.py .
zip -r ../daily-balance-lambda.zip .
cd ..
```

2. **Create Lambda function**
   - Go to AWS Lambda Console
   - Create new function (Python 3.13)
   - Upload the zip file
   - Set handler to: `main.lambda_handler`
   - Set timeout to 30-60 seconds

3. **Configure environment variables**
   - `PLAID_CLIENT_ID`
   - `PLAID_SECRET`
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_NUMBER`
   - `USER_PHONE`

4. **Set up EventBridge trigger**
   - Add EventBridge trigger to Lambda
   - Create schedule rule with cron expression
   - Example: `cron(0 14 * * ? *)` for 9 AM EST daily

## Project Structure
```
daily-balance/
├── src/
│   ├── main.py           # Entry point with lambda_handler
│   ├── banking.py        # Plaid API integration
│   └── msg.py            # Twilio API integration
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```


## Notes

- Currently uses Plaid Sandbox for development/demo purposes
- WhatsApp notifications via Twilio sandbox
- EventBridge schedule can be disabled when not in active use

## Author

Nikhil Jain