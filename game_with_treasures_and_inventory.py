import pygame
import random
import time

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 616
SCREEN_HEIGHT = 660

cell_size = SCREEN_WIDTH//28
cell_number = SCREEN_HEIGHT//30

pygame.init()

text_font = pygame.font.SysFont('Broadway', 60)
victory = text_font.render("You won!", True, (255,255,255))
loss = text_font.render("You lost!", True, (255,255,255))

victoryRect = victory.get_rect()
victoryRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

lossRect = loss.get_rect()
lossRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((12, 12))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Treasure(pygame.sprite.Sprite):
    def __init__(self,color,index):
        super(Treasure, self).__init__()
        self.index = index
        self.color = color
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT),
            )
        )


class Inventory(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((72, 12))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
score = []
inventory = Inventory()

# Create groups to hold treasure sprites and all sprites
# - treasures is used for collision detection and position updates
# - all_sprites is used for rendering

treasures = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

red = (255,0,0)
yellow = (255,255,0)
green = (50, 200, 0)
blue = (0,0,255)

# CREATING TREASURES
for i in range(5):      # YELLOW TREASURES
    yellow_treasure = Treasure(yellow,i)
    treasures.add(yellow_treasure)
    all_sprites.add(yellow_treasure)

for i in range(5):      # GREEN TREASURES
    green_treasure = Treasure(green,i)
    treasures.add(green_treasure)
    all_sprites.add(green_treasure)

for i in range(5):      # BLUE TREASURES
    blue_treasure = Treasure(blue,i)
    treasures.add(blue_treasure)
    all_sprites.add(blue_treasure)

for i in range(5):      # RED TREASURES
    red_treasure = Treasure(red,i)
    treasures.add(red_treasure)
    all_sprites.add(red_treasure)

inv = pygame.sprite.Group()

# Variable to keep the main loop running
running = True

# Main loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    for x in range((SCREEN_WIDTH//cell_number)*2):
        pygame.draw.line(screen, (0,0,90), (x*cell_number/2, 0), (x*cell_number/2, SCREEN_HEIGHT))
    for x in range((SCREEN_HEIGHT//cell_size)*2):
        pygame.draw.line(screen, (0,0,90), (0, x*cell_size/2),(SCREEN_WIDTH, x*cell_size/2))

    collided = pygame.sprite.spritecollide(player, treasures, True)

    for object in collided:
        if len(inv) < 7:
            inv.add(object)

    screen.blit(inventory.surf, (272,645))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    for i in range(7):
        try:
            inventory.surf.blit(inv.sprites()[i].surf, (1+i*11,1))
        except IndexError:
            pass

    # ENDS GAME WHEN THE INVENTORY IS FULL
    if len(inv) == 7:
        running = False

    # Update the display
    pygame.display.flip()

# CALCULATING THE SCORE
for i in range(7):
    score.append(inv.sprites()[i].color)

red_counter = 0
yellow_counter = 0
green_counter = 0
blue_counter = 0

for color in score:
    if color == red:
        red_counter += 1
    elif color == yellow:
        yellow_counter += 1
    elif color == green:
        green_counter += 1
    elif color == blue:
        blue_counter += 1

# DISPLAYS THE OUTCOME
while True:

    screen.fill((0, 0, 0))

    if red_counter == 5 or yellow_counter == 5 or green_counter == 5 or blue_counter == 5:
        screen.blit(victory, victoryRect)
    else:
        screen.blit(loss, lossRect)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
