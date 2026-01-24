import random

while True:
    try:
        x = int(input("How many frames do you own: "))
        if x <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

quota = random.randint(0, x)
print(f"Python chose #{quota}")
