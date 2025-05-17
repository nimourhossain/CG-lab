import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))  # Number of steps

    x_inc = dx / steps  # X increment per step
    y_inc = dy / steps  # Y increment per step

    x_points = []
    y_points = []

    for i in range(steps + 1):
        x_points.append(round(x))  # Round to nearest pixel
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points

# Example usage
x1, y1 = 2, 3
x2, y2 = 15, 10
x_points, y_points = DDA(x1, y1, x2, y2)

# Plotting the result
plt.plot(x_points, y_points, marker='o', color='blue')
plt.title("DDA Line Drawing")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.show()
