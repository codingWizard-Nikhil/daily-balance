import os  
from msg import create_message
from banking import get_balance

def main():  
    """Main function that can be called locally or from Lambda"""
    name, balance = get_balance()
    create_message(name, balance)
    return name, balance  

def lambda_handler(event, context):  
    """Lambda entry point"""
    try:
        name, balance = main()
        return {
            'statusCode': 200,
            'body': f'Successfully sent balance for {name}: ${balance}'
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }

# For local testing
if __name__ == "__main__":
    main() 


