from core import database


def login(card_number, pin):
    """Authenticate user based on card number and PIN."""
    user = database.get_user(card_number)
    if user and user["pin"] == pin:
        return True
    return False