import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Midpoint Circle Algorithm")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

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
        screen_pt = (pt[0] + 300, 300 - pt[1])  # center shift and y flip
        pygame.draw.circle(win, BLUE, screen_pt, 3)
        print(f"Point: {pt}")

def midpoint_circle(win, xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    plot_points(win, xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_points(win, xc, yc, x, y)

win.fill(WHITE)
midpoint_circle(win, 0, 0, 8)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
