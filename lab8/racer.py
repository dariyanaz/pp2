import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Load background image
background = pygame.image.load('AnimatedStreet.png')

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.SysFont("Verdana", 60)  # Font for "Game Over" message
font_small = pygame.font.SysFont("Verdana", 20)  # Small font for score display
game_over = font.render("Game Over", True, BLACK)

# Get screen size from background image dimensions
WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car game")


SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
clock = pygame.time.Clock()  # Initialize clock for frame rate control

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Coin.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -40))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > HEIGHT:
            self.rect.top = random.randint(-100, -40)
            self.rect.centerx = random.randint(40, WIDTH - 40)

# Create player and enemy objects
P1 = Player()
E1 = Enemy()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)  # Add enemy to the enemy group

coins = pygame.sprite.Group()
for _ in range(1):  # Create only 1 coin
    coins.add(Coin())

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)  # Add player to the group
all_sprites.add(E1)  # Add enemy to the group

# Create a custom event for increasing speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw the background

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2  # Increase enemy speed every second
        if event.type == pygame.QUIT:
            running = False

    # Update and draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            entity.move()  # Move enemies
        else:
            entity.update()  # Update player position

    # Update and draw all coins
    for coin in coins:
        screen.blit(coin.image, coin.rect)
        coin.move()  # Move coin downward

        # Check for collision between the player and a coin
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += 1  # Increase the coin counter
            coin.rect.top = random.randint(-100, -40)  # Reset coin to appear from the top
            coin.rect.centerx = random.randint(40, WIDTH - 40)  # Place it at a new random position

    # Display the score (number of dodged enemies)
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))  # Display score at the top-left corner

    # Display collected coins count
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coins_text, (WIDTH - 100, 10))  # Display coins at the top-right corner

    # Check if player collides with an enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)
        screen.blit(game_over, (WIDTH//2 - 170, HEIGHT//2 - 30))  # Display "Game Over" message
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    FPS = 60
    clock.tick(FPS)

# Quit pygame and close the game window
pygame.quit()
sys.exit()