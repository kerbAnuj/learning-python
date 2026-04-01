#01_Guess.py
#Simple guessing game
#Code dated 30th of March, 2026

import random

low = int(input("Lower limit of guess range: "))
up = int(input("Upper limit of guess range (exclusive): "))

guess = ""
count = 0
jackpot = random.randrange(low, up)

while guess != jackpot:
    guess = int(input("Take a Guess!: "))
    diff = jackpot - guess
    
    if diff in [1,2,-1,-2]:
        print("Close!")
    elif guess == jackpot:
        count += 1
        break
    else:
        print("Incorrect!")
    
    count += 1

print(f"Great guess! You took {count} tries.")

