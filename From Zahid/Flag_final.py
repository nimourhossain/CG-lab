import pygame
import sys
import math

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Flag with Wave")

RED       = (255, 0, 0)
GREEN     = (0, 100, 0)
SKY_BLUE  = (135, 206, 235)
brown = (139, 69, 19)

flag_x, flag_y = 150, 100
flag_width, flag_height = 300, 200
circle_center = (flag_x + flag_width // 2, flag_y + flag_height // 2)
circle_radius = 50

wave_offset = 0

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(flag_width):
        wave_shift = int(10 * math.sin((x / 20) + wave_offset))
        pygame.draw.line(screen, GREEN, 
                         (flag_x + x, flag_y + wave_shift), 
                         (flag_x + x, flag_y + flag_height + wave_shift))

    pygame.draw.circle(screen, RED, circle_center, circle_radius)
    pygame.draw.rect(screen, brown, (flag_x - 10, flag_y, 10, 400))

    pygame.display.flip()
    wave_offset += 0.1
    clock.tick(60)

pygame.quit()
sys.exit()
