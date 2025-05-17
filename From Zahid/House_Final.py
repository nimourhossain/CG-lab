import pygame
import sys

#initialize pygame
pygame.init()

#setup the screen
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple House")

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 191, 255)
GRAY = (169, 169, 169)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

#Main loop
running = True
while running:
    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False

    #Draw the house base
    pygame.draw.rect(screen, BROWN, (200, 200, 200, 200))

    # Draw the roof
    pygame.draw.polygon(screen, RED, [(180, 200), (420, 200), (300, 100)])  # Triangle roof

    # Door
    pygame.draw.rect(screen, BLACK, (275, 300, 50, 100))

    # left window
    pygame.draw.rect(screen, WHITE, (225, 225, 50, 50))
    pygame.draw.rect(screen, BLACK, (241, 225, 1, 50))
    pygame.draw.rect(screen, BLACK, (258, 225, 1, 50))
    pygame.draw.rect(screen, BLACK, (225, 241, 50, 1))
    pygame.draw.rect(screen, BLACK, (225, 258, 50, 1))

    #Right display
    pygame.draw.rect(screen, WHITE, (325, 225, 50, 50))
    pygame.draw.rect(screen, BLACK, (341, 225, 1, 50))
    pygame.draw.rect(screen, BLACK, (358, 225, 1, 50))
    pygame.draw.rect(screen, BLACK, (325, 241, 50, 1))
    pygame.draw.rect(screen, BLACK, (325, 258, 50, 1))




    #update display
    pygame.display.flip()

# exit code
pygame.quit()
sys.exit()