import random

print("=== Random Weapon Picker ===")
print("Enter how many weapons you own in each category:\n")

# Get number of primary weapons
while True:
    try:
        primary_count = int(input("How many primary weapons do you own: "))
        if primary_count <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# Get number of secondary weapons
while True:
    try:
        secondary_count = int(input("How many secondary weapons do you own: "))
        if secondary_count <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# Get number of melee weapons
while True:
    try:
        melee_count = int(input("How many melee weapons do you own: "))
        if melee_count <= 0:
            print("Please enter a positive number!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

# Generate random weapon selections
primary_choice = random.randint(1, primary_count)
secondary_choice = random.randint(1, secondary_count)
melee_choice = random.randint(1, melee_count)

# Display results
print("\n" + "=" * 22)
print("Your Random Loadout:")
print(f"Primary Weapon #{primary_choice}")
print(f"Secondary Weapon #{secondary_choice}")
print(f"Melee Weapon #{melee_choice}")
print("=" * 22)
