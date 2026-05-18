# Simple Snake Game using pygame
# Install pygame first:
# pip install pygame

import pygame
import random
import sys

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Snake initial position
snake = [(100, 100)]
dx, dy = BLOCK, 0

# Food position
food = (
    random.randrange(0, WIDTH, BLOCK),
    random.randrange(0, HEIGHT, BLOCK)
)

score = 0

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -BLOCK
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, BLOCK
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -BLOCK, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = BLOCK, 0

    # Move snake
    head_x = snake[0][0] + dx
    head_y = snake[0][1] + dy
    new_head = (head_x, head_y)

    # Game over conditions
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake
    ):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1
        food = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK)
        )
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], BLOCK, BLOCK))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK, BLOCK))

    draw_text(f"Score: {score}", WHITE, 10, 10)

    pygame.display.update()
    clock.tick(10)