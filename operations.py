from data import accounts, users
import datetime

def deposit(account_name, amount):
    """Deposit money into an account."""
    if account_name in accounts:
        if amount > 0:
            accounts[account_name]["balance"] += amount
            accounts[account_name]["transactions"].append(f"Deposited {amount}")
            print(f"Successfully deposited {amount} to {account_name}.")
        else:
            print("Amount must be greater than 0.")
    else:
        print("Account not found.")

def withdraw(account_name, amount):
    """Withdraw money from an account."""
    if account_name in accounts:
        if 0 < amount <= accounts[account_name]["balance"]:
            accounts[account_name]["balance"] -= amount
            accounts[account_name]["transactions"].append(f"Withdrew {amount}")
            print(f"Successfully withdrew {amount} from {account_name}.")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("Account not found.")

def transfer(source_account, destination_account, amount):
    """Transfer money from one account to another."""
    if source_account in accounts and destination_account in accounts:
        if 0 < amount <= accounts[source_account]["balance"]:
            accounts[source_account]["balance"] -= amount
            accounts[destination_account]["balance"] += amount
            accounts[source_account]["transactions"].append(f"Transferred {amount} to {destination_account}")
            accounts[destination_account]["transactions"].append(f"Received {amount} from {source_account}")
            print(f"Successfully transferred {amount} from {source_account} to {destination_account}.")
        else:
            print("Insufficient funds or invalid amount.")
    else:
        print("One or both accounts not found.")

def deposit():
    """Prompt for account and deposit only 0.05, 0.10, or 0.25 into an account. Print a receipt after deposit."""
    account_name = input("Enter the account number: ")
    try:
        amount = float(input("Enter amount to deposit (0.05, 0.10, or 0.25 only): "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    allowed = [0.05, 0.10, 0.25]
    if account_name.isdigit():
        account_name = int(account_name)
    if account_name in accounts:
        if amount in allowed:
            accounts[account_name]["balance"] += amount
            accounts[account_name]["transactions"].append(f"Deposited {amount}")
            print(f"Successfully deposited {amount} to {account_name}.")
            # Find username associated with this account
            username = None
            for user, info in users.items():
                if "account_number" in info and account_name in info["account_number"]:
                    username = user
                    break
            now = datetime.datetime.now()
            print("\n--- Deposit Receipt ---")
            print(f"Transaction Type: Deposit")
            print(f"Account Number: {account_name}")
            print(f"Username: {username if username else 'Unknown'}")
            print(f"Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Amount Deposited: {amount}")
            print("----------------------\n")
        else:
            print("Only 0.05, 0.10, or 0.25 denominations are accepted.")
    else:
        print("Account not found.")