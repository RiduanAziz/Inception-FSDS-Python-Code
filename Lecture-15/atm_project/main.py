from core import auth
from core import transactions


def main():
    print("Welcome to the Python ATM!")
    #1. User Authentication
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")

    if auth.login(card_number, pin):
        print(f"\nLogin successful! Welcome, user {card_number}.")
        while True:
            print("\nPlease choose an option:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                balance = transactions.check_balance(card_number)
                print(f"Your current balance is: ${balance}")

            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                new_balance = transactions.withdraw(card_number, amount)
                if new_balance is not None:
                    print(f"Withdrawal successful! Your new balance is: ${new_balance}")
            
            elif choice == '3':
                print("Thank you for using the Python ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid card number or PIN. Please try again.")

if __name__ == "__main__":
    main()