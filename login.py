import json

# Open and load the JSON data
with open('account.json', 'r') as file:
    account_data = json.load(file)

# Now you can access your data as a Python dictionary
print(account_data)

def login():
    print("=== Login ===")
