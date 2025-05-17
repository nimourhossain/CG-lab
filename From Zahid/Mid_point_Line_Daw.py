import matplotlib.pyplot as plt

def midpoint_line(x0, y0, x1, y1):
    x_points = []
    y_points = []

    dx = x1 - x0
    dy = y1 - y0

    x = x0
    y = y0

    p = dy - (dx / 2)  # initial decision parameter

    x_points.append(x)
    y_points.append(y)

    while x < x1:
        x += 1
        if p < 0:
            p += dy
        else:
            y += 1
            p += dy - dx

        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

# Example usage (slope must be between 0 and 1)
x0, y0 = 2, 3
x1, y1 = 15, 10
x_points, y_points = midpoint_line(x0, y0, x1, y1)

# Plot the line
plt.plot(x_points, y_points, marker='o', color='orange')
plt.title("Mid-Point Line Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()
