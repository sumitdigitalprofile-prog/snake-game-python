import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")


BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


snake = [(300, 200), (290, 200), (280, 200)]
direction = (10, 0)


food = (
    random.randrange(0, WIDTH, 10),
    random.randrange(0, HEIGHT, 10)
)

clock = pygame.time.Clock()
running = True

while running:

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, 10):
                direction = (0, -10)

            elif event.key == pygame.K_DOWN and direction != (0, -10):
                direction = (0, 10)

            elif event.key == pygame.K_LEFT and direction != (10, 0):
                direction = (-10, 0)

            elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                direction = (10, 0)

   
    head_x, head_y = snake[0]
    dx, dy = direction

    new_head = (head_x + dx, head_y + dy)
    snake.insert(0, new_head)

   
    if new_head == food:
        food = (
            random.randrange(0, WIDTH, 10),
            random.randrange(0, HEIGHT, 10)
        )
    else:
        snake.pop()

    
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        running = False


    screen.fill(BLACK)

    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0], segment[1], 10, 10)
        )

    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], 10, 10)
    )

    pygame.display.update()

    clock.tick(10)

pygame.quit()
