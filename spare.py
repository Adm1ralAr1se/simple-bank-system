from data import users, accounts

def view_accounts():
    print("\n--- All User Accounts ---")
    for username, info in users.items():
        print(f"Username: {username}")
        print(f"  Locked: {info.get('locked', False)}")
        print(f"  Accounts: {info.get('account_number', [])}")
        print("")

def freeze_account(username):
    if username in users:
        users[username]["locked"] = True
        print(f"Account '{username}' has been frozen.")
    else:
        print("Username not found.")

def unfreeze_account(username):
    if username in users:
        users[username]["locked"] = False
        print(f"Account '{username}' has been unfrozen.")
    else:
        print("Username not found.")

def view_transaction_logs(account_number):
    if account_number in accounts:
        print(f"\n--- Transaction Log for Account {account_number} ---")
        for log in accounts[account_number]["transactions"]:
            print(log)
    else:
        print("Account number not found.")

# Example usage:
if __name__ == "__main__":
    view_accounts()
    freeze_account("user1")
    unfreeze_account("user1")
    view_transaction_logs(202501)