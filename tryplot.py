# Matplotlib Demo: Displaying a LaTeX Math Formula

import matplotlib.pyplot as plt

# Create a figure and axis
plt.figure(figsize=(6, 3))

# Display a LaTeX math formula
plt.text(0.5, 0.5, r'$\int_{0}^{\infty} e^{-x^2} \, dx = \frac{\sqrt{\pi}}{2}$',
         fontsize=10, ha='center', va='center')

# Remove axis for a clean display
plt.axis('off')

# Add title
plt.title("LaTeX Math Formula in Matplotlib")

# Show the plot
plt.show()
