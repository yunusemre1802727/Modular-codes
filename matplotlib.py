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

# Before latex expressions use r
# For example: r'$\alpha$ [$a_{ij}$]'

# Enclosing in Dollar Signs ($): Most LaTeX expressions are enclosed in dollar signs.
# For example, to write a Greek letter, you can use "$\alpha$", where \alpha is the LaTeX command for the Greek letter alpha.
# ----------------------------------------------------------------------

# Mathematical Symbols: Many mathematical symbols have LaTeX equivalents.
# For instance, ^ denotes exponentiation, so "$x^2$" would render as x².
# ----------------------------------------------------------------------

# Subscripts and Superscripts: You can use _ for subscripts and ^ for superscripts. 
# For example, "$a_{ij}$" for a subscript and "$b^2$" for a superscript.
# ----------------------------------------------------------------------

# Fractions: You can create fractions using \frac{numerator}{denominator}. 
# For instance, "$\frac{1}{2}$" would render as ½.
# ----------------------------------------------------------------------

# Roots: Use \sqrt for square roots.
# For example, "$\sqrt{2}$" would render as √2.
# ----------------------------------------------------------------------

# Special Characters: Some characters have special LaTeX commands.
# For example, "$\approx$" for the approximate symbol (≈).

# Alpha: $\alpha$
# Beta: $\beta$
# Gamma: $\gamma$
# Delta: $\delta$
# Epsilon: $\epsilon$
# Zeta: $\zeta$
# Eta: $\eta$
# Theta: $\theta$
# Iota: $\iota$
# Kappa: $\kappa$
# Lambda: $\lambda$
# Mu: $\mu$
# Nu: $\nu$
# Xi: $\xi$
# Omicron: $o$ (Note: Omicron is commonly represented by the letter 'o' without a backslash)
# Pi: $\pi$
# Rho: $\rho$
# Sigma: $\sigma$
# Tau: $\tau$
# Upsilon: $\upsilon$
# Phi: $\phi$
# Chi: $\chi$
# Psi: $\psi$
# Omega: $\omega$
