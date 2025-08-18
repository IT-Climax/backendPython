import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBJECT_WIDTH = 50
OBJECT_HEIGHT = 50
MAX_FALL_SPEED = 5
OBJECT_FALL_RATE = 2

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


# Falling Object class
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBJECT_WIDTH, OBJECT_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
        self.rect.y = random.randint(-150, -OBJECT_HEIGHT)
        self.fall_speed = random.randint(1, MAX_FALL_SPEED)

    def update(self):
        self.rect.y += self.fall_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-150, -OBJECT_HEIGHT)
            self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECT_WIDTH)
            self.fall_speed = random.randint(1, MAX_FALL_SPEED)


# Initialize player and groups
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

falling_objects = pygame.sprite.Group()

# Add initial falling objects
for i in range(5):
    falling_object = FallingObject()
    all_sprites.add(falling_object)
    falling_objects.add(falling_object)

# Set up game clock
clock = pygame.time.Clock()

# Game loop
running = True
score = 0
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Update all sprites
    all_sprites.update(keys)

    # Check for collision
    if pygame.sprite.spritecollide(player, falling_objects, True):
        print(f"Game Over! Final Score: {score}")
        running = False

    # Increase difficulty
    score += 1
    if score % 500 == 0:
        MAX_FALL_SPEED += 1
        OBJECT_FALL_RATE += 1
        for obj in falling_objects:
            obj.fall_speed = random.randint(1, MAX_FALL_SPEED)

    # Draw all sprites
    all_sprites.draw(screen)

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()

# Start the game
#guess_the_word()
print(f' the sum of the dictionary is {sum}')
print(f' the sum of the square is {sum_the_square}')
print(f'the sum of the square is {sum_value}')
print(f'the average of the value is: {sum_value/i}')
print(f'the dictionary is: {my_dict}')
    
    
