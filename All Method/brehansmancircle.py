import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bresenham Circle Algorithm")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def plot_points(win, xc, yc, x, y):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    ]
    for pt in points:
        screen_pt = (pt[0] + 300, 300 - pt[1])  # Shift and flip y to center and correct direction
        pygame.draw.circle(win, RED, screen_pt, 4)
        print(f"Point: {pt}")

def bresenham_circle(win, xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    plot_points(win, xc, yc, x, y)

    while x <= y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        plot_points(win, xc, yc, x, y)

win.fill(WHITE)
bresenham_circle(win, 0, 0, 8)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 