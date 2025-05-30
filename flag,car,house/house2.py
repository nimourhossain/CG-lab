import pygame
pygame.init()

# Window setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Easy House")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)
RED = (200, 0, 0)
BLUE = (0, 191, 255)

# Draw function
def draw_house():
    screen.fill(WHITE)
    
    # House base
    pygame.draw.rect(screen, BROWN, (200, 200, 200, 150))  # x, y, width, height
    
    # Roof
    pygame.draw.polygon(screen, RED, [(200, 200), (300, 120), (400, 200)])  # triangle

    # Door
    pygame.draw.rect(screen, BLACK, (275, 275, 50, 75))

    # Windows
    pygame.draw.rect(screen, BLUE, (220, 220, 40, 40))
    
    pygame.draw.rect(screen, BLUE, (340, 220, 40, 40))

# Main loop
running = True
while running:
    draw_house()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
