import os  
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.products import Products


try:
    import config
    plaid_client_id = config.plaid_id
    plaid_secret = config.plaid_secret
except ImportError:
    plaid_client_id = os.environ.get('PLAID_CLIENT_ID')
    plaid_secret = os.environ.get('PLAID_SECRET')

# Create the Plaid client
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': plaid_client_id, 
        'secret': plaid_secret,  
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# Generate sandbox public_token
pt_request = SandboxPublicTokenCreateRequest(
    institution_id="ins_109508",
    initial_products=[Products('transactions')]
)
pt_response = client.sandbox_public_token_create(pt_request)
public_token = pt_response['public_token']

# Exchange for access_token
exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']

def get_balance():
    balance_request = AccountsBalanceGetRequest(access_token=access_token)
    balance_response = client.accounts_balance_get(balance_request)
    accounts = balance_response['accounts']
    account_name = accounts[0]['name']
    account_balance = accounts[0]['balances']['current']
    return account_name, account_balance