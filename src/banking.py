
import config
import plaid
from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_balance_get_request import AccountsBalanceGetRequest
from plaid.model.products import Products

# 1. Create the Plaid client 
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': config.plaid_id,
        'secret': config.plaid_secret,
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# 2. Generate a sandbox public_token (simulates a user linking their bank)
pt_request = SandboxPublicTokenCreateRequest(
    institution_id="ins_109508",            # Plaid's test bank
    initial_products=[Products('transactions')]
)
pt_response = client.sandbox_public_token_create(pt_request)
public_token = pt_response['public_token']

# 3. Exchange the public_token for an access_token (needed for all future calls)
exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']

# 4. Function to get the balance
def get_balance():
    balance_request = AccountsBalanceGetRequest(access_token=access_token)
    balance_response = client.accounts_balance_get(balance_request)
    accounts = balance_response['accounts']
    account_name = accounts[0]['name']
    account_balance = accounts[0]['balances']['current']
    return account_name, account_balance

# 5. Quick test
#if __name__ == "__main__":
    name, balance = get_balance()
    print(f"Account: {name} | Balance: ${balance}")
