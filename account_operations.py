from data import accounts, users

def account_creation():
    """Create a new account."""
    print("=== Account Creation ===")
    username = input("Enter your username: ")
    if username in users:
        print(f"Username '{username}' already exists. Please choose a different username.")
        return None
    

    new_password = input("Enter a 4 digit pin for your account: eg. 1234: ")
    if len(new_password) != 4 or not new_password.isdigit():
        print("Invalid password. Please enter a 4-digit numeric PIN.")
        return None 

    
    new_account_number = max(accounts.keys()) + 1
    accounts[new_account_number] = {"balance": 0.05, "transactions": ["Initial deposit: 0.05"]}
    
    users[username] = {
        "password": new_password,
        "account_number": [new_account_number],
        "locked": False
    }
    
    accounts[new_account_number] = {
        "balance": 0.0,
        "transactions": []
    }
    
    print(f"Account created successfully for user '{username}' with account number {new_account_number}.")
    return username, new_account_number