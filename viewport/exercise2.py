import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray-Triangle Intersection Visualization")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Coordinate transformation
def transform(point):
    return int(WIDTH // 2 + point[0] * 100), int(HEIGHT // 2 - point[1] * 100)

# Triangle vertices
A = (1, 0, 0)
B = (0, 1, 0)
C = (0, 0, 1)

# Ray origin and direction
O = (1, 1, 1)
D = (-1, -1, -1)

# Calculate intersection using Möller–Trumbore
Edge1 = [B[i] - A[i] for i in range(3)]
Edge2 = [C[i] - A[i] for i in range(3)]
h = [
    D[1]*Edge2[2] - D[2]*Edge2[1],
    D[2]*Edge2[0] - D[0]*Edge2[2],
    D[0]*Edge2[1] - D[1]*Edge2[0]
]
a = sum(Edge1[i] * h[i] for i in range(3))
f = 1 / a
s = [O[i] - A[i] for i in range(3)]
u = f * sum(s[i] * h[i] for i in range(3))
q = [
    s[1]*Edge1[2] - s[2]*Edge1[1],
    s[2]*Edge1[0] - s[0]*Edge1[2],
    s[0]*Edge1[1] - s[1]*Edge1[0]
]
v = f * sum(D[i] * q[i] for i in range(3))
t = f * sum(Edge2[i] * q[i] for i in range(3))

# Intersection point
intersection = [O[i] + t * D[i] for i in range(3)]

# 2D projection (x, y only)
A_2D = transform((A[0], A[1]))
B_2D = transform((B[0], B[1]))
C_2D = transform((C[0], C[1]))
O_2D = transform((O[0], O[1]))
I_2D = transform((intersection[0], intersection[1]))

# Draw loop
screen.fill(WHITE)
pygame.draw.polygon(screen, BLUE, [A_2D, B_2D, C_2D], 2)
pygame.draw.circle(screen, GREEN, O_2D, 6)
pygame.draw.circle(screen, RED, I_2D, 6)
pygame.draw.line(screen, BLACK, O_2D, I_2D, 1)

font = pygame.font.SysFont(None, 24)
text = font.render(f"t={t:.2f}, u={u:.2f}, v={v:.2f}, w={1 - u - v:.2f}", True, BLACK)
screen.blit(text, (10, 10))

pygame.display.flip()

# Wait until close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
