import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bresenham Line with Steps")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def bresenham(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    p = 2 * dy - dx
    x, y = x0, y0
    print(f"Start: ({x}, {y})")
    points.append((x, y))

    while x < x1:
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            y += 1
            p += 2 * dy - 2 * dx
        print(f"Point: ({x}, {y})")
        points.append((x, y))
    return points

start = (1, 1)
end =(5, 4)
scale = 100

points = bresenham(*start, *end)

win.fill(WHITE)

for pt in points:
    pygame.draw.circle(win, RED, (pt[0]*scale, pt[1]*scale), 6)

for i in range(len(points) - 1):
    pygame.draw.line(win, BLACK,
                     (points[i][0]*scale, points[i][1]*scale),
                     (points[i+1][0]*scale, points[i+1][1]*scale), 2)

pygame.draw.circle(win, BLACK, (start[0]*scale, start[1]*scale), 8)
pygame.draw.circle(win, BLACK, (end[0]*scale, end[1]*scale), 8)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
