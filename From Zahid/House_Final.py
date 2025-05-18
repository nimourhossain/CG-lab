import pygame
import sys

# initialize pygame
pygame.init()

# setup the screen
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple House")

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 191, 255)
GRAY = (169, 169, 169)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

# Main loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the house base
    pygame.draw.rect(screen, BROWN, (200, 200, 200, 200))

    # Draw the roof
    pygame.draw.polygon(screen, RED, [(180, 200), (420, 200), (300, 100)])  # Triangle roof

    # Door (centered with space on both sides)
    door_width = 60
    door_height = 180
    door_x = 270  # (200 + 200 - 60) / 2 = 270
    door_y = 210
    pygame.draw.rect(screen, BLACK, (door_x, door_y, door_width, door_height))

    # Left window (with space from door and edge)
    pygame.draw.rect(screen, WHITE, (215, 230, 40, 40))
    pygame.draw.line(screen, BLACK, (235, 230), (235, 270), 1)
    pygame.draw.line(screen, BLACK, (215, 250), (255, 250), 1)

    # Right window (with space from door and edge)
    pygame.draw.rect(screen, WHITE, (345, 230, 40, 40))
    pygame.draw.line(screen, BLACK, (365, 230), (365, 270), 1)
    pygame.draw.line(screen, BLACK, (345, 250), (385, 250), 1)

    # update display
    pygame.display.flip()

# exit code
pygame.quit()
sys.exit()
