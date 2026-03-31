import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# --- Top surface (plane) ---
x = np.linspace(0, 3, 100)
y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x, y)

Z = 6 - X - Y
mask = (X + Y <= 3)
Z = np.where(mask, Z, np.nan)

ax.plot_surface(X, Y, Z, alpha=0.7)

# --- Bottom (triangle) ---
ax.plot_trisurf(
    [0, 3, 0],
    [0, 0, 3],
    [0, 0, 0],
    alpha=0.4
)

# --- Side 1 (x = 0 plane) ---
y_side = np.linspace(0, 3, 50)
z_side = np.linspace(0, 6, 50)
Y_side, Z_side = np.meshgrid(y_side, z_side)
X_side = np.zeros_like(Y_side)

# Keep only valid region
mask_side = (Z_side <= 6 - Y_side)
Z_side = np.where(mask_side, Z_side, np.nan)

ax.plot_surface(X_side, Y_side, Z_side, alpha=0.4)

# --- Side 2 (y = 0 plane) ---
x_side = np.linspace(0, 3, 50)
z_side = np.linspace(0, 6, 50)
X_side, Z_side = np.meshgrid(x_side, z_side)
Y_side = np.zeros_like(X_side)

mask_side = (Z_side <= 6 - X_side)
Z_side = np.where(mask_side, Z_side, np.nan)

ax.plot_surface(X_side, Y_side, Z_side, alpha=0.4)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Solid Volume under z = 6 - x - y')

plt.show()
