import matplotlib.pyplot as plt
import numpy as np

# Generate example datasets
x = np.array( [1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
y2 = np.array([3, 5, 7, 9, 11])
y3 = np.array([1, 3, 5, 7, 9])

# Calculate average and standard deviation
average_y     = np.mean([y1, y2, y3], axis=0)
std_deviation = np.std( [y1, y2, y3], axis=0)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the average line
ax.plot(x, average_y, label='Average', color='blue')

# Fill between the upper and lower bounds of standard deviation
ax.fill_between(x, average_y - std_deviation, average_y + std_deviation, color='black', alpha=0.2, label='Deviation')

# Plot individual datasets
ax.plot(x, y1, label='Dataset 1', marker='o')
ax.plot(x, y2, label='Dataset 2', marker='s')
ax.plot(x, y3, label='Dataset 3', marker='^')

# Set labels and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Show the plot
plt.show()
