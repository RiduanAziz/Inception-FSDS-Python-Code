import random

jackpot = random.randint(1,100)

# print(jackpot)

guess_number = int(input("Enter your guess number: "))

couunter = 1

while guess_number != jackpot:

    if guess_number < jackpot:
        print("Wrong! Please guess higher")

    else:
        print("Wrong! Please guess lower")

    guess_number = int(input("Enter your guess number: "))
    couunter += 1

else:
    print("Correct Guess")
    print("Your attempt is: ", couunter)
