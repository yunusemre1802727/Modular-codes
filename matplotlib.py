import matplotlib.pyplot as plt
from matplotlib import rc

output_figure_name = "example.png"

x = [0, 1, 2, 3]
y1 = [0, 1, 4, 9]
y2 = [0, 1, 9, 25]

# Set font properties globally
rc('font', family='serif', serif='Times New Roman', size=14)  # Runtime Configuration

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # (a,b) a inches wide, b inches high

# Plot some data with a label
ax.plot(x, y1, label=r'$\alpha$ [$a_{ij}$]')
ax.scatter(x, y2, label=r'$\beta$ [$\frac{1}{s}$]')

# Set tick parameters to make tick lines inward
ax.tick_params(axis='both', direction='in', length=6, width=2)

# Set axis labels
ax.set_xlabel("a")
ax.set_ylabel('b')

# Add legend
ax.legend()

# Remove the grid
ax.grid(False)

# Save figure
plt.savefig(f"{output_figure_name}", dpi=300)        

# Close the figure
plt.show()
