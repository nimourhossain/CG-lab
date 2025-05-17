import pygame
pygame.init()

w, h = 600, 600
win = pygame.display.set_mode((w, h))
origin = (w//2, h//2)

def to_screen(x, y):
    return (origin[0] + x, origin[1] - y)

def draw(points, color):
    pts = [to_screen(x, y) for x, y in points]
    pygame.draw.polygon(win, color, pts, 2)
    for p in pts:
        pygame.draw.circle(win, color, p, 3)

shape = [(0, 0), (50, 0), (50, 50), (0, 50)]
scaled = [(x * 1.5, y * 0.5) for x, y in shape]

win.fill((0, 0, 0))
pygame.draw.line(win, (255, 255, 255), (0, origin[1]), (w, origin[1]))
pygame.draw.line(win, (255, 255, 255), (origin[0], 0), (origin[0], h))
draw(shape, (255, 0, 0))
draw(scaled, (0, 255, 0))
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
