import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colormaps

# Create the repeating pattern 4,3,2,1 for numbers 1 to 50
numbers = list(range(1, 51))
pattern = [4, 3, 2, 1]
pattern_values = [pattern[i % 4] for i in range(len(numbers))]

# Create figure with multiple subplots
fig = plt.figure(figsize=(15, 10))
fig.suptitle(
    "Warframe Disruption - Rotation Pattern (4,3,2,1)",
    fontsize=16,
    fontweight="bold",
    y=0.98,
)

# 1. Basic table view
ax1 = plt.subplot(2, 2, 1)
ax1.axis("tight")
ax1.axis("off")
table_data = []
for i in range(0, 50, 10):
    for j in range(10):
        idx = i + j
        if idx < 50:
            table_data.append([numbers[idx], pattern_values[idx]])

table = ax1.table(
    cellText=table_data,
    colLabels=["Round", "Pattern"],
    colColours=["#2E86C1", "#2E86C1"],
    cellColours=[
        ["#F2F2F2", "#F2F2F2"] if i % 2 == 0 else ["#E8E8E8", "#E8E8E8"]
        for i in range(len(table_data))
    ],
    loc="center",
    cellLoc="center",
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)
ax1.set_title("Pattern Values", pad=20)

# 2. Line plot
ax2 = plt.subplot(2, 2, 2)
ax2.plot(
    numbers,
    pattern_values,
    marker="o",
    linestyle="-",
    color="#E74C3C",
    linewidth=2,
    markersize=6,
    markeredgecolor="black",
)
ax2.set_xlabel("Round Number", fontsize=12)
ax2.set_ylabel("Pattern Value", fontsize=12)
ax2.set_title("Pattern Progression", fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.set_xticks(range(0, 51, 5))
ax2.set_yticks(range(1, 5))

# Add pattern labels on the line
for i, (x, y) in enumerate(zip(numbers, pattern_values)):
    if i % 10 == 0:  # Label every 10th point
        ax2.annotate(
            f"({x},{y})",
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=9,
        )

# 3. Heatmap style visualization
ax3 = plt.subplot(2, 2, 3)
pattern_matrix = np.array(pattern_values).reshape(10, 5)
im = ax3.imshow(pattern_matrix, cmap="coolwarm", aspect="auto")
ax3.set_title("Pattern Heatmap", fontsize=14)
ax3.set_xlabel("Column", fontsize=12)
ax3.set_ylabel("Row", fontsize=12)

# Add text annotations to heatmap
for i in range(10):
    for j in range(5):
        text = ax3.text(
            j,
            i,
            pattern_matrix[i, j],
            ha="center",
            va="center",
            color="white",
            fontweight="bold",
        )

# Add colorbar
cbar = plt.colorbar(im, ax=ax3)
cbar.set_label("Pattern Value", rotation=270, labelpad=15)

# 4. Bar chart grouped by pattern
ax4 = plt.subplot(2, 2, 4)
pattern_counts = {1: 0, 2: 0, 3: 0, 4: 0}
for val in pattern_values:
    pattern_counts[val] += 1

colors = ["#2E86C1", "#28B463", "#E74C3C", "#F39C12"]
bars = ax4.bar(
    pattern_counts.keys(), pattern_counts.values(), color=colors, edgecolor="black"
)
ax4.set_xlabel("Pattern Value", fontsize=12)
ax4.set_ylabel("Frequency (out of 50 rounds)", fontsize=12)
ax4.set_title("Pattern Frequency Distribution", fontsize=14)
ax4.set_xticks(list(pattern_counts.keys()))

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax4.text(
        bar.get_x()() + bar.get_width() / 2.0,
        height + 0.1,
        f"{height}",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

plt.tight_layout()
plt.show()

# Print table for quick reference
print("\n" + "=" * 60)
print("WARFRAME DISRUPTION - ROTATION PATTERN (4,3,2,1)")
print("=" * 60)
print(f"{'Round':<10} {'Pattern':<10} {'Next Reset':<15}")
print("-" * 35)

for i, (num, val) in enumerate(zip(numbers, pattern_values)):
    next_reset = "After 4 rounds" if (i + 1) % 4 == 0 else f"In {3 - (i % 4)} rounds"
    print(f"{num:<10} {val:<10} {next_reset:<15}")

    if (i + 1) % 10 == 0:  # Add separator every 10 rounds
        print("-" * 35)

print("=" * 60)
print("Rotation C every 4 rounds (Pattern: 4, 3, 2, 1 repeating)")
print("=" * 60)
