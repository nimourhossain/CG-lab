import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("HJHJH")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
BLUE = (0, 191, 255)
GRAY = (169, 169, 169)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

running = True

while running:
    screen.fill(GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
