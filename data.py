# Dictionary to store account balances and transaction histories
accounts = {
    202501: {"balance": 0.10, "transactions": []},
    202502: {"balance": 0.20, "transactions": []},
    202503: {"balance": 0.30, "transactions": []},
    202504: {"balance": 0.10, "transactions": []},
    202505: {"balance": 0.25, "transactions": []}
}

users = {
    "admin": {"password": "admin1234"},
    "user1": {"password": "2013", 
              "account_number": [202501, 202502, 202503],
              "locked": False
    },
    "user2": {"password": "3162", 
              "account_number": [202404, 202405],
              "locked": False
    }
}