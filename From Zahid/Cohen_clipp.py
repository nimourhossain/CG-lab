import matplotlib.pyplot as plt

# Region codes
INSIDE = 0     # 0000
LEFT = 1       # 0001
RIGHT = 2      # 0010
BOTTOM = 4     # 0100
TOP = 8        # 1000

# Compute region code for a point (x, y)
def compute_code(x, y, xmin, xmax, ymin, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
    code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0.0, 0.0
            out_code = code1 if code1 != 0 else code2

            if out_code & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif out_code & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif out_code & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif out_code & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if out_code == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, xmin, xmax, ymin, ymax)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, xmin, xmax, ymin, ymax)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# Visualization
if __name__ == "__main__":
    # Line to be clipped
    x1, y1 = 10, 10
    x2, y2 = 100, 100

    # Clipping window
    xmin, xmax = 20, 80
    ymin, ymax = 20, 80

    # Apply clipping
    clipped = cohen_sutherland_clip(x1, y1, x2, y2, xmin, xmax, ymin, ymax)

    # Plotting
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Draw clipping window
    clip_rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                              edgecolor='blue', facecolor='none', linestyle='--', linewidth=2)
    ax.add_patch(clip_rect)
    plt.text(xmin + 1, ymin - 5, 'Clipping Window', color='blue')

    # Original line
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle=':', label='Original Line')

    # Clipped line
    if clipped:
        xc1, yc1, xc2, yc2 = clipped
        ax.plot([xc1, xc2], [yc1, yc2], color='green', linewidth=2, label='Clipped Line')
    else:
        print("Line is outside and rejected.")

    ax.legend()
    ax.set_title("Cohen-Sutherland Line Clipping")
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 120)
    plt.grid(True)
    plt.show()
