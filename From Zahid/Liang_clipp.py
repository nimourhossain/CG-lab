import matplotlib.pyplot as plt

def liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Parallel and outside
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, r)
            else:
                u2 = min(u2, r)

    if u1 > u2:
        return None

    x1_clip = x1 + u1 * dx
    y1_clip = y1 + u1 * dy
    x2_clip = x1 + u2 * dx
    y2_clip = y1 + u2 * dy

    return (x1_clip, y1_clip, x2_clip, y2_clip)

# Example usage and visualization
if __name__ == "__main__":
    # Original line
    x1, y1 = 10, 10
    x2, y2 = 100, 100

    # Clipping window bounds
    xmin, xmax = 20, 80
    ymin, ymax = 20, 80

    # Get clipped line
    clipped = liang_barsky(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

    # Plotting
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Draw clipping window
    clip_rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                              edgecolor='blue', facecolor='none', linestyle='--', linewidth=2)
    ax.add_patch(clip_rect)
    plt.text(xmin + 1, ymin - 5, 'Clipping Window', color='blue')

    # Draw original line
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle=':', label='Original Line')

    # Draw clipped line (if exists)
    if clipped:
        xc1, yc1, xc2, yc2 = clipped
        ax.plot([xc1, xc2], [yc1, yc2], color='red', linewidth=2, label='Clipped Line')
    else:
        print("Line is outside the clipping window and rejected.")

    ax.legend()
    ax.set_title("Liang-Barsky Line Clipping")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 120)
    plt.grid(True)
    plt.show()
