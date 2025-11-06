"""
Excrtise-1
ATM Machine Menu

1. Pin Change
2. Balance Check
3. Withdraw
4. Deposit
5. Exit
"""
menu = input("""
Hi there! Welcome to ATM
Please Choose,

1. Enter 1 for Pin Change
2. Enter 2 for Balance Check
3. Enter 3 for Withdraw
4. Enter 4 for Deposit
5. Enter 5 for Exit             
""")

if menu == "1":
    print("Pin Change")

elif menu == "2":
    print("Balance Check")

elif menu == "3":
    print("Withdraw")

elif menu == "4":
    print("Deposit")

else:
    print("Exit")
