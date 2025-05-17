import matplotlib.pyplot as plt

def midpoint_circle(cx, cy, r):
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter
    points = []

    while x <= y:
        # 8 symmetric points around the center
        points.extend([
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x),
        ])

        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

    return points

# Example usage:
center_x, center_y = 0, 0
radius = 10
circle_points = midpoint_circle(center_x, center_y, radius)

# Plotting
x_vals, y_vals = zip(*circle_points)
plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='red')
plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
