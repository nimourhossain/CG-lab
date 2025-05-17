import pygame
import sys
import math

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car on Road with Moving Leaf Trees and Sun")

# Colors
SKY_BLUE = (135, 206, 235)
ROAD_COLOR = (50, 50, 50)
GRASS_COLOR = (34, 139, 34)
TREE_BG_COLOR = (139, 69, 19)  # brown soil color behind trees
TREE_TRUNK = (101, 67, 33)
TREE_LEAVES = (34, 139, 34)
CAR_COLOR = (255, 0, 0)
BLACK = (0, 0, 0)
SUN_YELLOW = (255, 223, 0)

clock = pygame.time.Clock()

car_x = -120
car_y = 250
car_speed = 5

angle = 0  # leaf offset angle (no change now)

def draw_tree(x, y, leaf_offset):
    pygame.draw.rect(screen, TREE_TRUNK, (x, y, 20, 40))
    center_x = x + 10
    center_y = y
    offset = int(5 * math.sin(leaf_offset))
    pygame.draw.circle(screen, TREE_LEAVES, (center_x - 10 + offset, center_y - 10), 20)
    pygame.draw.circle(screen, TREE_LEAVES, (center_x + offset, center_y - 30), 25)
    pygame.draw.circle(screen, TREE_LEAVES, (center_x + 10 + offset, center_y - 10), 20)

def draw_car(x, y):
    pygame.draw.rect(screen, CAR_COLOR, (x, y, 100, 40))
    pygame.draw.circle(screen, BLACK, (x + 20, y + 40), 12)
    pygame.draw.circle(screen, BLACK, (x + 80, y + 40), 12)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SKY_BLUE)  # sky

    pygame.draw.circle(screen, SUN_YELLOW, (width - 80, 80), 50)  # sun

    pygame.draw.rect(screen, GRASS_COLOR, (0, height//2 + 20, width, height//2 - 20))  # grass

    pygame.draw.rect(screen, TREE_BG_COLOR, (0, 220, width, 60))  # brown soil behind trees

    pygame.draw.rect(screen, ROAD_COLOR, (0, 280, width, 100))  # road

    for tx in range(50, width, 150):
        draw_tree(tx, 240, angle)

    draw_car(car_x, car_y)

    car_x += car_speed
    if car_x > width:
        car_x = -120

    # angle += 0.1   Commented out to stop leaf movement

    pygame.display.update()
    clock.tick(60)
