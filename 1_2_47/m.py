import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (np.sin(2*x)**2) / ((x - np.pi/2)**2)

# Create x values avoiding division by zero
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
x = x[x != np.pi/2]

# Compute y values
y = f(x)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r"$f(x) = \frac{\sin^2(2x)}{(x - \frac{\pi}{2})^2}$")

# Plot the limit point
plt.scatter([np.pi/2], [4], color='red', zorder=5, label="Point (π/2, 4)")

# Horizontal dashed line for limit
plt.axhline(4, linestyle='--', color='red', label="Limit = 4")

# Labels and title
plt.title("Broad View of f(x) with Oscillations")
plt.xlabel("x")
plt.ylabel("f(x)")

# Grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()
