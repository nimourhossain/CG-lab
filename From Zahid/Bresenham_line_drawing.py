import matplotlib.pyplot as plt

def bresenham_with_p(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    x, y = x1, y1

    # Assume slope m <= 1
    p = 2 * dy - dx  # Initial decision parameter
    two_dy = 2 * dy
    two_dy_dx = 2 * (dy - dx)

    while x <= x2:
        x_points.append(x)
        y_points.append(y)

        if p < 0:
            p += two_dy
            
        else:
            y += 1
            p += two_dy_dx

        x += 1

    return x_points, y_points

# Example usage (only works for x2 > x1 and 0 ≤ slope ≤ 1)
x1, y1 = 1, 1
x2, y2 = 5, 4
x_points, y_points = bresenham_with_p(x1, y1, x2, y2)

# Plotting the result
plt.plot(x_points, y_points, marker='o', color='green')
plt.title("Bresenham's Line (Using Decision Parameter p)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.axis("equal")
plt.show()
