import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enhanced House Drawing")

# Define colors
WHITE = (255, 255, 255)
LIGHT_BROWN = (160, 82, 45)  # Lighter brown for the door
PALE_SKY_BLUE = (160, 210, 240)  # Light sky-like blue

RED = (178, 34, 34)
BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
TAN = (210, 180, 140)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)  # Sky background

    # Draw grass
    pygame.draw.rect(screen, GREEN, (0, 500, width, 100))

    # Draw house base
    house_rect = pygame.Rect(300, 300, 200, 200)
    pygame.draw.rect(screen, TAN, house_rect)

    # Draw roof
    roof_points = [(250, 300), (550, 300), (400, 200)]
    pygame.draw.polygon(screen, LIGHT_BROWN, roof_points)

    # Draw chimney
    chimney_rect = pygame.Rect(450, 220, 30, 80)
    pygame.draw.rect(screen, LIGHT_BROWN, chimney_rect)

    # Adjusted door size (reduced from top and bottom)
    door_width = 50
    door_height = 170  # Reduced from 200
    door_rect = pygame.Rect(400 - door_width // 2, 320, door_width, door_height)
    pygame.draw.rect(screen, PALE_SKY_BLUE, door_rect)

    # Upper triangle (downward)
    triangle_height = 20  # Smaller height for triangles
    door_top = [
        (door_rect.left, door_rect.top),
        (door_rect.right, door_rect.top),
        (door_rect.centerx, door_rect.top + triangle_height)
    ]
    pygame.draw.polygon(screen, BLACK, door_top, 1)

    # Lower triangle (upward)
    door_bottom = [
        (door_rect.left, door_rect.bottom),
        (door_rect.right, door_rect.bottom),
        (door_rect.centerx, door_rect.bottom - triangle_height)
    ]
    pygame.draw.polygon(screen, BLACK, door_bottom, 1)

    # Vertical middle line on the door
    pygame.draw.line(screen, BLACK,
                     (door_rect.centerx, door_rect.top + triangle_height),
                     (door_rect.centerx, door_rect.bottom - triangle_height), 1)

    # Draw side black lines on the door
    pygame.draw.line(screen, BLACK, (door_rect.left, door_rect.top), (door_rect.left, door_rect.bottom), 1)
    pygame.draw.line(screen, BLACK, (door_rect.right, door_rect.top), (door_rect.right, door_rect.bottom), 1)

    # Draw door handle
    pygame.draw.circle(screen, BLACK, door_rect.center, 4)

    # Draw windows
    for x_pos in [310, 440]:
        # Window frame
        pygame.draw.rect(screen, BLACK, (x_pos - 2, 348, 54, 54), 2)
        # Window glass
        pygame.draw.rect(screen, WHITE, (x_pos, 350, 50, 50))
        # Cross bars
        pygame.draw.line(screen, BLACK, (x_pos + 25, 350), (x_pos + 25, 400), 2)
        pygame.draw.line(screen, BLACK, (x_pos, 375), (x_pos + 50, 375), 2)

    # Draw stairs
    stair_colors = [GRAY, (150, 150, 150), (170, 170, 170)]
    for i in range(3):
        stair_rect = pygame.Rect(380 - (i * 10), 500 + (i * 20), 40 + (i * 20), 20)
        pygame.draw.rect(screen, stair_colors[i], stair_rect)

    # Draw sun with rays
    pygame.draw.circle(screen, YELLOW, (100, 100), 50)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        end_x = 100 + 70 * math.cos(rad)
        end_y = 100 + 70 * math.sin(rad)
        pygame.draw.line(screen, YELLOW, (100, 100), (end_x, end_y), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()
