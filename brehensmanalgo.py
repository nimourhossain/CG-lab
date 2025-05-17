import pygame

def bresenham_line(x1, y1, x2, y2, screen, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    if dy <= dx:
        err = dx / 2.0
        while x != x2:
            screen.set_at((x, y), color)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
        screen.set_at((x, y), color)
    else:
        err = dy / 2.0
        while y != y2:
            screen.set_at((x, y), color)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
        screen.set_at((x, y), color)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Bresenham Line Drawing")
screen.fill((255, 255, 255))

# Draw line
start = (100, 100)
end = (400, 300)
bresenham_line(start[0], start[1], end[0], end[1], screen, (0, 0, 0))

pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
