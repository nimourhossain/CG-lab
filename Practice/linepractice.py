import pygame
import sys
import math

# --------------------------------------------------
# 1. Initialize Pygame
# --------------------------------------------------
pygame.init()

# --------------------------------------------------
# 2. Screen Setup
# --------------------------------------------------
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Flag with Wave")

# --------------------------------------------------
# 3. Colors (RGB)
# --------------------------------------------------
RED       = (255, 0, 0)
GREEN     = (0, 100, 0)
SKY_BLUE  = (135, 206, 235)
brown = (139, 69, 19)

# --------------------------------------------------
# 4. Flag Dimensions and Position
# --------------------------------------------------
flag_x, flag_y = 150, 100
flag_width, flag_height = 300, 200
circle_center = (flag_x + flag_width // 2, flag_y + flag_height // 2)
circle_radius = 50

# --------------------------------------------------
# 5. Main Loop
# --------------------------------------------------
wave_offset = 0  # controls wave animation

running = True
clock = pygame.time.Clock()

while running:
    # Fill background with sky blue
    screen.fill(SKY_BLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw waving green rectangle (flag body)
    for x in range(flag_width):
        # Calculate vertical wave offset for this x
        wave_shift = int(10 * math.sin((x / 20) + wave_offset))
        # Draw vertical line shifted vertically by wave_shift
        pygame.draw.line(screen, GREEN, 
                         (flag_x + x, flag_y + wave_shift), 
                         (flag_x + x, flag_y + flag_height + wave_shift))

    # Draw red circle (static)
    pygame.draw.circle(screen, RED, circle_center, circle_radius)

    # Draw black flag pole
    pygame.draw.rect(screen, brown, (flag_x - 10, flag_y, 10, 400))

    # Draw black pole base
    # pygame.draw.rect(screen, brown, (flag_x - 25, flag_y + 400, 40, 50))

    # Update the display
    pygame.display.flip()

    # Update wave offset for animation
    wave_offset += 0.1

    # Cap frame rate to 60 FPS
    clock.tick(60)

# Quit pygame properly
pygame.quit()
sys.exit()