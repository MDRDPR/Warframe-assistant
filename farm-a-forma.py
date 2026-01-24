import random


f = int(input("Guess a number between 20 and 0:"))

x = random.randint(0, 20)

if x == f:
    print(f"Correct it was {x}")
    print("Congrats!!!")
else:
    print("You lose: Farm a Forma!!")
    print(f"Wrong!!! It was {x}")
