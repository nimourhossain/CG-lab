import matplotlib.pyplot as plt

def bresenham_circle(center_x, center_y, radius):
    x = 0
    y = radius
    p = 3 - 2 * radius  # Initial decision parameter
    points = []

    while x <= y:
        # Add all eight symmetrical points of the circle
        points.extend([
            (center_x + x, center_y + y),
            (center_x - x, center_y + y),
            (center_x + x, center_y - y),
            (center_x - x, center_y - y),
            (center_x + y, center_y + x),
            (center_x - y, center_y + x),
            (center_x + y, center_y - x),
            (center_x - y, center_y - x),
        ])

        # Update decision parameter and points
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Example usage:
center_x, center_y = 0, 0
radius = 10
circle_points = bresenham_circle(center_x, center_y, radius)

# Separate x and y for plotting
x_vals, y_vals = zip(*circle_points)

plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='blue')
plt.title("Bresenham's Circle Drawing")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
