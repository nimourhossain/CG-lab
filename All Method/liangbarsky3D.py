import pygame
import sys

def liang_barsky_3d(x1, y1, z1, x2, y2, z2, xmin, xmax, ymin, ymax, zmin, zmax):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    p = [-dx, dx, -dy, dy, -dz, dz]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1, z1 - zmin, zmax - z1]

    u1, u2 = 0.0, 1.0

    for i in range(6):
        print(f"Step {i+1}: p={p[i]}, q={q[i]}, u1={u1}, u2={u2}")
        if p[i] == 0:
            if q[i] < 0:
                print("Line is parallel and outside clipping volume.")
                return None
        else:
            u = q[i] / p[i]
            if p[i] < 0:
                if u > u2:
                    print("Reject line (u > u2)")
                    return None
                if u > u1:
                    u1 = u
                    print(f"Update u1: {u1}")
            else:
                if u < u1:
                    print("Reject line (u < u1)")
                    return None
                if u < u2:
                    u2 = u
                    print(f"Update u2: {u2}")

    clipped_start = (x1 + u1 * dx, y1 + u1 * dy, z1 + u1 * dz)
    clipped_end = (x1 + u2 * dx, y1 + u2 * dy, z1 + u2 * dz)

    print(f"Clipped segment: {clipped_start} to {clipped_end}")
    return clipped_start, clipped_end

# Pygame setup
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("3D Liang-Barsky Clipping (2D Projection)")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define clipping cube boundaries
xmin, xmax = 100, 500
ymin, ymax = 100, 500
zmin, zmax = 0, 100  # z range (depth)

# Define 3D line points
start_3d = (50, 50, 50)
end_3d = (550, 550, 120)

clipped_line = liang_barsky_3d(*start_3d, *end_3d, xmin, xmax, ymin, ymax, zmin, zmax)

def project_3d_to_2d(point3d):
    # Simple orthographic projection ignoring z
    x, y, z = point3d
    return int(x), int(y)

win.fill(WHITE)

# Draw clipping rectangle (projection of clipping cube on XY plane)
pygame.draw.rect(win, GREEN, (xmin, ymin, xmax - xmin, ymax - ymin), 2)

# Draw original line (projected)
pygame.draw.line(win, RED, project_3d_to_2d(start_3d), project_3d_to_2d(end_3d), 2)

# Draw clipped line if it exists
if clipped_line:
    p_start = project_3d_to_2d(clipped_line[0])
    p_end = project_3d_to_2d(clipped_line[1])
    pygame.draw.line(win, BLACK, p_start, p_end, 4)

pygame.display.update()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
