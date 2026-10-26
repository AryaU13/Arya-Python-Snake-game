import pygame
import random

pygame.init()

cell = 40
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

snake = [(5, 5)]
food = (7, 5)
direction = "R"
score = 0
game_over = False

foods = [(7, 5), (0, 0)]

def show_game():
    screen.fill((0, 0, 0))

    for x in range(10):
        for y in range(10):
            pygame.draw.rect(
                screen, (100, 100, 100),
                (x * cell, y * cell, cell, cell), 1
            )

    pygame.draw.rect(
        screen, (255, 0, 0),
        (food[0] * cell, food[1] * cell, cell, cell)
    )

    for x, y in snake:
        pygame.draw.rect(
            screen, (0, 255, 0),
            (x * cell, y * cell, cell - 2, cell - 2)
        )

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (5, 5))

    if game_over:
        text = font.render("GAME OVER! Score: " + str(score),
                           True, (255, 255, 0))
        screen.blit(text, (50, 180))

    pygame.display.update()

def move_snake():
    global food, score, game_over

    x, y = snake[0]

    if direction == "R":
        x += 1
    elif direction == "L":
        x -= 1
    elif direction == "U":
        y -= 1
    elif direction == "D":
        y += 1

    head = (x, y)

    if x < 0 or x > 9 or y < 0 or y > 9:
        game_over = True
        print("Game Over! Wall hit at", head)
        print("Final score:", score)
        return

    eating = head == food
    body = snake if eating else snake[:-1]

    if head in body:
        game_over = True
        print("Game Over! Snake collision.")
        print("Final score:", score)
        return

    snake.insert(0, head)

    if eating:
        score += 10
        print("Food eaten at", food, "! Score:", score)

        if len(foods) > 0:
            food = foods.pop(0)
        else:
            while True:
                new_food = (random.randint(0, 9),
                            random.randint(0, 9))
                if new_food not in snake:
                    food = new_food
                    break
    else:
        snake.pop()

    print("Head:", snake[0], "| Length:", len(snake))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            key = event.key

            keys = {
                pygame.K_RIGHT: "R",
                pygame.K_LEFT: "L",
                pygame.K_UP: "U",
                pygame.K_DOWN: "D"
            }

            if key in keys:
                new_direction = keys[key]

                opposite = {
                    "R": "L", "L": "R",
                    "U": "D", "D": "U"
                }

                if new_direction == opposite[direction]:
                    print("Reverse move not allowed.")
                else:
                    direction = new_direction
                    move_snake()

    show_game()
    clock.tick(30)

pygame.quit()