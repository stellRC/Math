heights = [30.0, 19.0, 11.3, 6.70, 4.0]

#common ratio from measured drop heights
common_ratio = ((heights[1] / heights[0]) + (heights[2] / heights[1]) + (heights[3] / heights [2]) + (heights[4] / heights [3])) / 4

print(f"Initial height (h_0): {heights[0]:.3f}")

print(f"Common ratio (r): {common_ratio:.3f}")

theoretic_distance = heights[0] + 2 * heights[0] * common_ratio / (1 - common_ratio)

print(f"Theoretical total distance (infinite bounces): {theoretic_distance:.3f}")




# Loop to calculate the distance for each subsequent bounce
number_of_bounces = 0

current_height = heights[0]

total_distance = current_height

for i in range(number_of_bounces):
    current_height *= common_ratio

    total_distance += 2 * current_height

    heights.append(round(current_height, 1))


   



print(f"Total vertical distance traveled after {number_of_bounces} bounces: {total_distance:.2f}")
print(f"Height {heights}")


# --- Plotting the Results ---
bounce_numbers = range(len(heights))

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()

ax.plot(bounce_numbers, heights, marker='o', linestyle='--', color='b', label='Bounce Height')
ax.set_xlabel("Bounce Number (0 = Initial Drop)")
ax.set_ylabel("Peak Height")
ax.set_title("Bouncing Ball Simulation")
ax.grid(True)
ax.legend()

# Add a horizontal line for the floor
ax.axhline(0, color='black', linewidth=0.75)

plt.show()