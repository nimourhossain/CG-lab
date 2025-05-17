import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Liang-Barsky Line Clipping")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clipping window boundaries
x_min, y_min = 100, 100
x_max, y_max = 500, 300

def liang_barsky(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]

    u1, u2 = 0.0, 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel and outside the boundary
        else:
            u = q[i] / p[i]
            if p[i] < 0:
                if u > u2:
                    return None
                if u > u1:
                    u1 = u
            else:
                if u < u1:
                    return None
                if u < u2:
                    u2 = u

    clipped_x1 = x1 + u1 * dx
    clipped_y1 = y1 + u1 * dy
    clipped_x2 = x1 + u2 * dx
    clipped_y2 = y1 + u2 * dy

    return (int(clipped_x1), int(clipped_y1)), (int(clipped_x2), int(clipped_y2))

# Original line (partially outside clipping window)
line_start = (50, 50)
line_end = (550, 350)

clipped_line = liang_barsky(*line_start, *line_end, x_min, y_min, x_max, y_max)

win.fill(WHITE)

# Draw clipping window
pygame.draw.rect(win, BLACK, (x_min, y_min, x_max - x_min, y_max - y_min), 2)

# Draw original line in RED
pygame.draw.line(win, RED, line_start, line_end, 2)

# Draw clipped line in GREEN if exists
if clipped_line:
    pygame.draw.line(win, GREEN, clipped_line[0], clipped_line[1], 3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
