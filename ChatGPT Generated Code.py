import pygame
from pygame.math import Vector2

# Initialize Pygame
pygame.init()

# Define the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define the size and initial position of the snake's head
snake_size = 20
head_position = Vector2(screen_width // 2, screen_height // 2)

# Define the initial direction of the snake
direction = Vector2(1, 0)  # Initial direction: right

clock = pygame.time.Clock()

# Initialize the snake's body as an array of segments
snake_body = [
    head_position,
    head_position - (direction * snake_size),
    head_position - (direction * 2 * snake_size)
]

game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Check for arrow key presses to change the direction of the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction.x != 1:  # Avoid reversing direction
                direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT and direction.x != -1:
                direction = Vector2(1, 0)
            elif event.key == pygame.K_UP and direction.y != 1:
                direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN and direction.y != -1:
                direction = Vector2(0, 1)

    # Update the position of the snake's head based on the current direction
    head_position += direction * snake_size

    # Create a new segment for the head and add it to the beginning of the snake's body
    snake_body.insert(0, head_position)

    # Remove the last segment of the snake's body
    snake_body.pop()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment.x, segment.y, snake_size, snake_size))

    # Update the display
    pygame.display.update()

    # Set the frame rate of the game
    clock.tick(10)

# Quit the game
pygame.quit()