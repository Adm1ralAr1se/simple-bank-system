from data import accounts, users

def account_statement(account_name):
    """Generate and display an account statement."""
    if account_name in accounts:
        print(f"\nAccount Statement for {account_name}:")
        print(f"Current Balance: {accounts[account_name]['balance']}")
        print("Transaction History:")
        for transaction in accounts[account_name]["transactions"]:
            print(f"- {transaction}")
    else:
        print("Account not found.")

def check_balance(account_name):
    """Check the current balance of an account."""
    if account_name in accounts:
        print(f"Current Balance for {account_name}: {accounts[account_name]['balance']}")
    else:
        print("Account not found.")
