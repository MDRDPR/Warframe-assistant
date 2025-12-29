import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps

# Create the repeating pattern 4,3,2,1 for numbers 1 to 50
# fro Warframe disruption Rotation C change 51 below for higher round if needed
numbers = list(range(1, 51))
pattern = [4, 3, 2, 1]


print("Number : Pattern")
print("----------------")
for i, num in enumerate(numbers):
    pattern_value = pattern[i % 4]  # 4 is the length of the pattern
    print(f"{num:6} : {pattern_value}")
