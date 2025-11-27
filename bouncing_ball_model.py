# Bouncing Ball & Geometric Series Simulation

# import matplotlib.pyplot as plt
initial_height = 30.0
measured_heights = [initial_height, 19.0, 11.3, 6.70, 4.0]

# Common ratio from measured drop measured_heights
common_ratio = ((measured_heights[1] / initial_height) + (measured_heights[2] / measured_heights[1]) + (measured_heights[3] / measured_heights [2]) + (measured_heights[4] / measured_heights [3])) / 4

print(f"Initial height: {measured_heights[0]:.2f}")
print(f"All Measured Heights: {measured_heights}")


print(f"Common ratio: {common_ratio:.3}")

# Geometric series formula
theoretic_distance = initial_height + (2 * initial_height * common_ratio) / (1 - common_ratio)

print(f"Theoretical total distance: {theoretic_distance:.2f}")

# Loop to calculate the distance for each subsequent bounce
bounce_count = 5

total_distance = current_height = initial_height

sim_height = [initial_height]


for i in range(bounce_count):
    
    # Height of next bounce
    current_height *= common_ratio

    total_distance += 2 * current_height
    
    sim_height.append(round(current_height, 3))
    
print(f"Total vertical distance traveled after {bounce_count} bounces: {total_distance:.2f}")
print(f"Simulated bounce measured_heights {sim_height}")
print(f"Difference btw simulation and theoretical distance: {abs(theoretic_distance - total_distance):.3f}")
print(f"Percent Error {abs(total_distance - theoretic_distance ) / theoretic_distance * 100:.1f}%")



# Uncomment for Colab

# sim_bounce = range(len(sim_height))
# true_bounce = range(len(measured_heights))

# plt.style.use('seaborn-v0_8-whitegrid')
# fig, ax = plt.subplots()

# ax.plot(sim_bounce, sim_height, marker='o', linestyle='--', color='b', label='Simulated Bounce Height')
# ax.plot(true_bounce, measured_heights, marker='*', linestyle='--', color='g', label='Theoretical Bounce Height')
# ax.set_xlabel("Bounce Number")
# ax.set_ylabel("Peak Height")
# ax.set_title("Bouncing Ball Simulation")
# ax.grid(True)
# ax.legend()

# # Add a horizontal line for the floor
# ax.axhline(0, color='black', linewidth=0.75)

# plt.show()