import pygame
import sys
import math

pygame.init()

# Screen setup
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bangladesh Flag with Realistic Wave")

# Colors
GREEN = (0, 106, 78)
RED = (244, 42, 65)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
DARK_GRAY = (80, 80, 80)

# Clock
clock = pygame.time.Clock()

def draw_flag_wave():
    base_x = 200
    base_y = 50
    flag_width = 260
    flag_height = 150
    pole_height = 450
    wave_amplitude = 10
    wave_length = 40

    # Draw tall flagpole
    pygame.draw.rect(screen, BLACK, (base_x - 10, base_y, 10, pole_height))

    # Draw waving green flag
    strip_height = 5
    for i in range(0, flag_height, strip_height):
        offset = math.sin(pygame.time.get_ticks() / 600 + i / wave_length) * wave_amplitude
        pygame.draw.polygon(
            screen,
            GREEN,
            [
                (base_x + offset, base_y + i),
                (base_x + flag_width + offset, base_y + i),
                (base_x + flag_width + offset, base_y + i + strip_height),
                (base_x + offset, base_y + i + strip_height)
            ]
        )

    # Red circle follows wave of middle height
    mid_offset = math.sin(pygame.time.get_ticks() / 600 + (flag_height / 2) / wave_length) * wave_amplitude
    circle_x = base_x + flag_width * 0.5 + mid_offset
    circle_y = base_y + flag_height / 2
    pygame.draw.circle(screen, RED, (int(circle_x), int(circle_y)), 40)

    # Cement base centered under pole
    base_top = base_y + pole_height
    base_center_x = base_x - 25
    pygame.draw.rect(screen, DARK_GRAY, (base_center_x, base_top, 60, 20))    # top part
    pygame.draw.rect(screen, GRAY, (base_center_x - 10, base_top + 20, 80, 30))  # bottom part

# Main loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_flag_wave()

    pygame.display.update()
    clock.tick(60)
