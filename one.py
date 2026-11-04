# Import pygame library to create the game
import pygame

# Import random library to generate random food
import random

# Initialize pygame
pygame.init()

# Set the size of each snake and food block
cell = 40

# Create a game window of 400x400 pixels
screen = pygame.display.set_mode((400, 400))

# Set the title of the game window
pygame.display.set_caption("Snake Game")

# Create a clock to control game speed
clock = pygame.time.Clock()

# Set the font for displaying text
font = pygame.font.SysFont(None, 25)

# Set the initial position of the snake
snake = [(5, 5)]

# Set the initial position of the food
food = (7, 5)

# Set the initial direction of the snake to Right
direction = "R"

# Set the initial score to zero
score = 0

# Set the game over status to False
game_over = False

# Create a list of fixed food positions
foods = [(7, 5), (0, 0)]


# Define a function to display the game objects
def show_game():

    # Fill the game screen with black colour
    screen.fill((0, 0, 0))

    # Loop through the X-coordinates of the grid
    for x in range(10):

        # Loop through the Y-coordinates of the grid
        for y in range(10):

            # Draw grey grid lines on the screen
            pygame.draw.rect(
                screen, (100, 100, 100),
                (x * cell, y * cell, cell, cell), 1
            )

    # Draw the food in red colour
    pygame.draw.rect(
        screen, (255, 0, 0),
        (food[0] * cell, food[1] * cell, cell, cell)
    )

    # Loop through each part of the snake
    for x, y in snake:

        # Draw the snake in green colour
        pygame.draw.rect(
            screen, (0, 255, 0),
            (x * cell, y * cell, cell - 2, cell - 2)
        )

    # Create the score text in white colour
    text = font.render("Score: " + str(score), True, (255, 255, 255))

    # Display the score on the screen
    screen.blit(text, (5, 5))

    # Check whether the game is over
    if game_over:

        # Create the game over message with the final score
        text = font.render("GAME OVER! Score: " + str(score),
                           True, (255, 255, 0))

        # Display the game over message
        screen.blit(text, (50, 180))

    # Update the display screen
    pygame.display.update()


# Define a function to move the snake
def move_snake():

    # Allow the function to modify global variables
    global food, score, game_over

    # Get the current position of the snake's head
    x, y = snake[0]

    # Move the snake one step to the right
    if direction == "R":
        x += 1

    # Move the snake one step to the left
    elif direction == "L":
        x -= 1

    # Move the snake one step upward
    elif direction == "U":
        y -= 1

    # Move the snake one step downward
    elif direction == "D":
        y += 1

    # Store the new head position
    head = (x, y)

    # Check whether the snake hits the wall
    if x < 0 or x > 9 or y < 0 or y > 9:

        # Set the game over status to True
        game_over = True

        # Print the wall collision position
        print("Game Over! Wall hit at", head)

        # Print the final score
        print("Final score:", score)

        # Stop the function
        return

    # Check whether the snake eats the food
    eating = head == food

    # Set the body for collision checking
    body = snake if eating else snake[:-1]

    # Check whether the snake hits its own body
    if head in body:

        # Set the game over status to True
        game_over = True

        # Print the collision message
        print("Game Over! Snake collision.")

        # Print the final score
        print("Final score:", score)

        # Stop the function
        return

    # Add the new head to the beginning of the snake
    snake.insert(0, head)

    # Check whether the snake has eaten the food
    if eating:

        # Increase the score by 10 points
        score += 10

        # Print the food position and updated score
        print("Food eaten at", food, "! Score:", score)

        # Check whether fixed food positions are available
        if len(foods) > 0:

            # Set the next food position from the list
            food = foods.pop(0)

        # Generate random food if the list is empty
        else:

            # Start a loop to generate new food
            while True:

                # Generate random X and Y coordinates
                new_food = (random.randint(0, 9),
                            random.randint(0, 9))

                # Check that food is not inside the snake
                if new_food not in snake:

                    # Set the new food position
                    food = new_food

                    # Exit the loop
                    break

    # If the snake has not eaten the food
    else:

        # Remove the last part of the snake
        snake.pop()

    # Print the head position and snake length
    print("Head:", snake[0], "| Length:", len(snake))


# Set the game running status to True
running = True

# Run the game while running is True
while running:

    # Check all game events
    for event in pygame.event.get():

        # Check whether the user closes the game window
        if event.type == pygame.QUIT:

            # Stop the game
            running = False

        # Check for keyboard input when the game is not over
        if event.type == pygame.KEYDOWN and not game_over:

            # Store the pressed key
            key = event.key

            # Create a dictionary for keyboard directions
            keys = {
                # Map the right arrow key to Right
                pygame.K_RIGHT: "R",

                # Map the left arrow key to Left
                pygame.K_LEFT: "L",

                # Map the up arrow key to Up
                pygame.K_UP: "U",

                # Map the down arrow key to Down
                pygame.K_DOWN: "D"
            }

            # Check whether the pressed key is valid
            if key in keys:

                # Store the new direction
                new_direction = keys[key]

                # Create a dictionary of opposite directions
                opposite = {
                    "R": "L", "L": "R",
                    "U": "D", "D": "U"
                }

                # Check whether the new direction is opposite
                if new_direction == opposite[direction]:

                    # Do not allow reverse movement
                    print("Reverse move not allowed.")

                # If the direction is valid
                else:

                    # Update the snake's direction
                    direction = new_direction

                    # Move the snake one step
                    move_snake()

    # Display the game objects
    show_game()

    # Set the game speed to 30 frames per second
    clock.tick(30)

# Close pygame properly
pygame.quit()
