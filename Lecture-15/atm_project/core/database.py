# A mock database of users
# Format: "Card Number": {"pin": "PIN", "balance": Amount}
users = {
    "1111": {"pin": "1234", "balance": 1000},
    "2222": {"pin": "9999", "balance": 500},
    "3333": {"pin": "0000", "balance": 100}
}

def get_user(card_number):
    """Fetch user details based on card number."""
    return users.get(card_number)
