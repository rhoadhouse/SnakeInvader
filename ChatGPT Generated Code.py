import pygame
import random

# Initialize Pygame
pygame.init()

# Define some constants for the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Create the player
player_img = pygame.image.load("player.png")
player_x = WINDOW_WIDTH // 2 - player_img.get_width() // 2
player_y = WINDOW_HEIGHT - player_img.get_height()
player_speed = 5

# Create the enemies
enemy_img = pygame.image.load("enemy.png")
enemies = []
for i in range(10):
    enemy_x = random.randint(0, WINDOW_WIDTH - enemy_img.get_width())
    enemy_y = random.randint(50, 200)
    enemies.append((enemy_x, enemy_y))

# Create the bullets
bullet_img = pygame.image.load("bullet.png")
bullets = []

# Create the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_img.get_width() // 2 - bullet_img.get_width() // 2
                bullet_y = player_y
                bullets.append((bullet_x, bullet_y))

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_img.get_width():
        player_x += player_speed

    # Move the bullets
    for bullet in bullets:
        bullet_x, bullet_y = bullet
        bullet_y -= 10
        bullet = (bullet_x, bullet_y)
        if bullet_y < 0:
            bullets.remove(bullet)
        else:
            bullet_rect = bullet_img.get_rect().move(bullet_x, bullet_y)
            for enemy in enemies:
                enemy_rect = enemy_img.get_rect().move(enemy)
                if bullet_rect.colliderect(enemy_rect):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    break

    # Move the enemies
    for i, enemy in enumerate(enemies):
        enemy_x, enemy_y = enemy
        enemy_x += random.randint(-5, 5)
        if enemy_x < 0:
            enemy_x = 0
        elif enemy_x > WINDOW_WIDTH - enemy_img.get_width():
            enemy_x = WINDOW_WIDTH - enemy_img.get_width()
        enemy_y += 5
        enemies[i] = (enemy_x, enemy_y)

    # Draw the screen
    screen.fill(BG_COLOR)
    screen.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)
    pygame.display.flip()

# Clean up
pygame.quit()