import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - 100
player_speed = 5
player = pygame.Rect(player_x, player_y, player_size, player_size)

# Enemy
enemy_size = 50
enemy_speed = 2
enemies = []

# Create enemies
def create_enemies():
    for row in range(3):
        for col in range(10):
            enemy_x = 50 * col + 50
            enemy_y = 50 * row + 50
            enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
            enemies.append(enemy)

create_enemies()

# Bullets
bullet_speed = 5
bullets = []

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player_size:
        player.x += player_speed

    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, enemy)

    for bullet in bullets:
        bullet.y -= bullet_speed
        pygame.draw.rect(screen, RED, bullet)

        # Remove bullet if it goes out of the screen
        if bullet.y < 0:
            bullets.remove(bullet)

        # Check for collision with enemies
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)

    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player.x + player_size // 2 - 2, player.y, 4, 10)
        bullets.append(bullet)

    pygame.draw.rect(screen, WHITE, player)

    pygame.display.flip()
#Dft