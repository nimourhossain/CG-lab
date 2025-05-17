import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Midpoint Line Algorithm")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def midpoint_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x, y = x0, y0
    points.append((x, y))
    print(f"Point: ({x}, {y})")

    while x < x1:
        if d < 0:
            d += dE
            x += 1
        else:
            d += dNE
            x += 1
            y += 1
        points.append((x, y))
        print(f"Point: ({x}, {y})")

    return points

start = (1, 1)
end = (5, 4)
points = midpoint_line(*start, *end)

win.fill(WHITE)

# Draw all points
for pt in points:
    pygame.draw.circle(win, RED, (pt[0]*100, pt[1]*100), 5)

# Draw lines between points
for i in range(len(points) - 1):
    pygame.draw.line(win, RED, (points[i][0]*100, points[i][1]*100), (points[i+1][0]*100, points[i+1][1]*100), 2)

# Draw start and end points bigger
pygame.draw.circle(win, BLACK, (start[0]*100, start[1]*100), 7)
pygame.draw.circle(win, BLACK, (end[0]*100, end[1]*100), 7)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
