from operations import deposit, withdraw, transfer
from statements import account_statement, check_balance
from login import login
from account_operations import account_creation
import json

accounts = {}
ACCOUNTS_FILE = "accounts.json"

# Bank Account Application
# This application allows users to manage their bank accounts, including depositing, withdrawing, and transferring money.
def main():
    """Main function to run the bank account application."""

    print("Welcome to the Bank Account Application!")
    while True:
        print("\nMenu:")
        print("1. Login as User")
        print("2. View Account Balance")
        print("3. Deposit Funds")
        print("4. Withdraw Funds")
        print("5. Manage Multiple Accounts")
        print("6. Transfer Funds Between Own Accounts")
        print("7. Transfer Funds to Another User")
        print("8. View Transaction History")
        print("9. Update your Personal Information")
        print("10. Login as Admin")
        print("11. Exit Application")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            login()
        
        elif choice == "2":
            account = input("Enter the account name (e.g., 202501): ")
            try:
                amount = float(input("Enter the amount to withdraw: "))
                withdraw(account, amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "3":
            source_account = input("Enter the source account name (e.g., 202501): ")
            destination_account = input("Enter the destination account name (e.g., 202502): ")
            try:
                amount = float(input("Enter the amount to transfer: "))
                transfer(source_account, destination_account, amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            account = input("Enter the account name (e.g., 202501): ")
            account_statement(account)
        
        elif choice == "5":
            account = input("Enter the account name (e.g., 202501): ")
            check_balance(account)

        elif choice == "6":
            account_creation()

        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()