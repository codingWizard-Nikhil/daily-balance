from msg import create_message
from banking import get_balance

if __name__ == "__main__":
    name, balance = get_balance()
    create_message(name, balance)




