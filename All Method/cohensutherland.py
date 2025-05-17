import pygame
import sys

pygame.init()
win = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Cohen-Sutherland Line Clipping")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define clip window
x_min, y_min = 100, 100
x_max, y_max = 500, 300

# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            x, y = 0, 0
            out_code = code1 if code1 != 0 else code2

            if out_code & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif out_code & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif out_code & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif out_code & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if out_code == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return (int(x1), int(y1)), (int(x2), int(y2))
    else:
        return None

# Original line (partially outside clip window)
line_start = (50, 50)
line_end = (550, 350)

clipped_line = cohen_sutherland_clip(*line_start, *line_end)

win.fill(WHITE)

# Draw clipping rectangle
pygame.draw.rect(win, BLACK, (x_min, y_min, x_max - x_min, y_max - y_min), 2)

# Draw original line in RED
pygame.draw.line(win, RED, line_start, line_end, 2)

# Draw clipped line in GREEN if it exists
if clipped_line:
    pygame.draw.line(win, GREEN, clipped_line[0], clipped_line[1], 3)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
