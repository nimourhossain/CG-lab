import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("DDA Line Algorithm")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def dda(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    print(f"Start: ({round(x)}, {round(y)})")
    points.append((round(x), round(y)))

    for i in range(int(steps)):
        x += x_inc
        y += y_inc
        print(f"Point: ({round(x)}, {round(y)})")
        points.append((round(x), round(y)))

    return points

start = (1, 1)
end = (5, 4)
points = dda(*start, *end)

win.fill(WHITE)

# Draw all points
for pt in points:
    pygame.draw.circle(win, RED, (pt[0]*100, pt[1]*100), 5)

# Draw lines between points
for i in range(len(points)-1):
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
