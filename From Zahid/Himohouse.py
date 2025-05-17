import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def apply_transformation(matrix, points):
    """Applies a transformation matrix to a set of 2D points."""
    return np.dot(matrix, points)

# Define the car body using homogeneous coordinates
car = np.array([
    [0, 4, 4, 0, 0],  # x-coordinates (body)
    [0, 0, 2, 2, 0],  # y-coordinates (body)
    [1, 1, 1, 1, 1]   # Homogeneous coordinates
])

# Define a wheel shape (a square for simplicity)
wheel = np.array([
    [-0.5, 0.5, 0.5, -0.5, -0.5],  # x-coordinates
    [-0.5, -0.5, 0.5, 0.5, -0.5],  # y-coordinates
    [1, 1, 1, 1, 1]   # Homogeneous coordinates
])

# Create two wheels at different positions
wheel1 = wheel.copy()
wheel2 = wheel.copy()
wheel1[0, :] += 1   # Position first wheel
wheel2[0, :] += 3   # Position second wheel
wheel1[1, :] -= 0.5 # Move down slightly
wheel2[1, :] -= 0.5 # Move down slightly

fig, ax = plt.subplots(figsize=(8, 5))

def update(frame):
    ax.clear()
    ax.set_xlim(-1, 15)
    ax.set_ylim(-2, 5)

    # Translation matrix for moving car
    translation_matrix = np.array([
        [1, 0, frame * 0.2],  # Move right over time
        [0, 1, 0],
        [0, 0, 1]
    ])

    # Rotation matrix for rotating wheels
    theta = -frame * 0.2  # Rotating counterclockwise as car moves
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Apply transformation to car body
    transformed_car = apply_transformation(translation_matrix, car)

    # Apply rotation to wheels about their center
    wheel1_center = np.array([[1], [-0.5], [1]])  # Center of wheel 1
    wheel2_center = np.array([[3], [-0.5], [1]])  # Center of wheel 2

    # Translate wheels to origin, rotate, then translate back
    wheel1_transformed = apply_transformation(rotation_matrix, wheel1 - wheel1_center) + wheel1_center
    wheel2_transformed = apply_transformation(rotation_matrix, wheel2 - wheel2_center) + wheel2_center

    # Apply car translation to rotated wheels
    transformed_wheel1 = apply_transformation(translation_matrix, wheel1_transformed)
    transformed_wheel2 = apply_transformation(translation_matrix, wheel2_transformed)

    # Plot car body
    ax.plot(transformed_car[0], transformed_car[1], 'b-', linewidth=3)
    # Plot rotating wheels
    ax.plot(transformed_wheel1[0], transformed_wheel1[1], 'ko-', linewidth=2)
    ax.plot(transformed_wheel2[0], transformed_wheel2[1], 'ko-', linewidth=2)

    ax.set_title("Moving Car with Rotating Wheels")

ani = animation.FuncAnimation(fig, update, frames=50, interval=100)
plt.show()