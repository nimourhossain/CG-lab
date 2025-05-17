import numpy as np
import matplotlib.pyplot as plt

def apply_transformation(matrix, points):
    """Applies a transformation matrix to a set of 2D points."""
    transformed_points = np.dot(matrix, points)
    return transformed_points

# Define a square (or any polygon) as a set of homogeneous coordinates
points = np.array([
    [0, 1, 1, 0, 0],  # x-coordinates
    [0, 0, 1, 1, 0],  # y-coordinates
    [1, 1, 1, 1, 1]   # Homogeneous coordinates
])

# Scaling Transformation
Sx, Sy = 2, 3
scaling_matrix = np.array([
    [Sx, 0, 0],
    [0, Sy, 0],
    [0, 0, 1]
])

# Shearing Transformation (X-direction)
Shx = 1.2
shearing_matrix = np.array([
    [1, Shx, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Rotation Transformation (90 degrees counterclockwise)
theta = np.radians(90)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

# Reflection across the X-axis
reflection_matrix_x = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]
])

# Apply transformations
scaled_points = apply_transformation(scaling_matrix, points)
sheared_points = apply_transformation(shearing_matrix, points)
rotated_points = apply_transformation(rotation_matrix, points)
reflected_points = apply_transformation(reflection_matrix_x, points)

# Plot the original and transformed shapes
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

def plot_shape(ax, original, transformed, title):
    """Plots the original and transformed shapes."""
    ax.plot(original[0], original[1], 'bo-', label="Original")
    ax.plot(transformed[0], transformed[1], 'r--', label="Transformed")
    ax.legend()
    ax.set_title(title)
    ax.grid()

plot_shape(axs[0, 0], points, scaled_points, "Scaling")
plot_shape(axs[0, 1], points, sheared_points, "Shearing")
plot_shape(axs[1, 0], points, rotated_points, "Rotation")
plot_shape(axs[1, 1], points, reflected_points, "Reflection")

plt.show()
