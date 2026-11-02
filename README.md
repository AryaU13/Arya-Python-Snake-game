Python Snake Game

## 1. Project Overview
The Snake Game is a simple 2D game developed using Python 3 and the Pygame library. The player controls a snake using keyboard keys to eat food. Whenever the snake eats food, its length increases and the score is updated. The game ends when the snake collides with the wall or itself.

## 2. Problem Statement
To develop a classic Snake Game using Python and Pygame in which the player steers a snake to eat food, increases its length and score, and avoids collisions with the wall or itself.

## 3. Objectives
- To understand basic Python programming concepts.
- To develop a simple interactive game using Pygame.
- To implement loops, lists, coordinates, and conditional statements.
- To handle keyboard input and game events.
- To implement food collection, score tracking, and collision detection.

## 4. Features
- Snake movement using keyboard controls.
- Food generation and collection.
- Snake growth after eating food.
- Score tracking.
- Wall and self-collision detection.
- Game Over condition.
- Interactive game window.

## 5. Technologies Used
- Programming Language: Python 3
- Library: Pygame
- IDE: Python IDLE / Visual Studio Code

## 6. Requirements
- Python 3 installed on the computer.
- Pygame library.
- Keyboard for controlling the snake.

Install Pygame using:

bash
pip install pygame


## 7. Input and Output

### Input
The player uses keyboard keys to control the snake:

- R / Right Arrow: Move Right
- L / Left Arrow: Move Left
- U / Up Arrow: Move Up
- D / Down Arrow: Move Down

Immediate reverse movement is not allowed.

### Output
The game displays a window containing the snake, food, and score. When the snake eats food, its length and score increase. If the snake hits a wall or itself, the game ends and displays the final score.

## 8. How to Execute the Project
1. Install Python 3.
2. Install the Pygame library.
3. Download the project files from GitHub.
4. Open the project folder in VS Code or Python IDLE.
5. Run the following command:

bash
python one.py


6. The Snake Game window will open.
7. Use the keyboard controls to play the game.

## 9. Test Cases

### Test Case 1: Normal Input
*Input:* Moves R, R

*Expected Output:*
- Snake moves to (6, 5) and then (7, 5).
- Food at (7, 5) is eaten.
- Score becomes 10.
- Snake length becomes 2.
- Head position becomes (7, 5).

### Test Case 2: Boundary / Minimum Input
*Input:* Moves R, R, R, R, R

*Expected Output:*
- Snake eats food at (7, 5).
- Score becomes 10.
- Snake reaches the boundary at (10, 5).
- Game Over is displayed.
- Final score is 10.

### Test Case 3: Invalid Input
*Input:*
(a) Press key X.
(b) Press L while the snake is moving Right.

*Expected Output:*
- Invalid key X is ignored.
- Immediate reverse movement is not allowed.
- Snake continues moving Right.

### Test Case 4: Different Valid Scenario
*Input:* Moves R, R, U, U

*Expected Output:*
- Snake eats food at (7, 5).
- Score becomes 10.
- Snake moves upward.
- Snake length becomes 2.
- Head position becomes (7, 3).

## 10. Testing and Validation
The project is tested using different keyboard inputs and game scenarios. The test cases check normal movement, boundary collision, invalid input, food collection, score updates, and game-over conditions.

Screenshots of the test inputs and corresponding outputs are provided in the testing screenshots PDF.

## 11. Conclusion
The Python Snake Game project demonstrates the use of Python programming and Pygame for developing a simple interactive game. It helps in understanding game logic, keyboard event handling, coordinate-based movement, collision detection, and score management.
