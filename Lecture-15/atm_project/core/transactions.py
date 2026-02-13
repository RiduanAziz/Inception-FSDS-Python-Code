from core import database

def check_balance(card_number):
    user = database.get_user(card_number)
    return user["balance"]


def withdraw(card_number, amount):
    user = database.get_user(card_number)
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return False
    if user["balance"] >= amount:
        user["balance"] -= amount
        return user["balance"]
    else:
        print("Insufficient balance.")
        return None