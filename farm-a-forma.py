import random

# Choose a number between 0 and 6
# If you choose incorrectly you get to farm a forma ;]
while True:
    try:
        f = int(input("Guess a number between 20 and 0:"))
        if f <= 0:
            print("Try a valid number")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

x = random.randint(0, 6)

if x == f:
    print("=" * 12)
    print(f"Correct it was {x}")
    print("Congrats!!!")
else:
    print("=" * 12)
    print("You lose: Farm a Forma!!")
    print(f"It was {x}")
